# Build a real-time auction bidding system
# System needs to serve relevant ads with <500ms

# What are other considerations in bidding?
# How to optimize autobidding budgets 
# Fraud prevention

# Overall system design 
# 1. Client. Users use UI to make bids on some auction
# 2. Proxy server. Receives request and routes to webserver
# 3. Web server. Receives routed request and writes to kv store 
# 4. KV store. Writes auction <> bid. Redis can manage sorted structs associated w/ keys using SortedSets 

# A. Scheduler service. Orchestrate transfer of kv-store auction deadline
# B. Async task queue. Makes request to worker boxes
# C. Worker. Makes write request to relational db 
# D. Relational DB. Updates auction entry

# About redundancy 
# We'd need to have 2 async replication, this is done every X minutes without bottlenecking main
# In case primary becomes unavailable, you can fallback to secondary 

# About performance
# We'd have replicas on the primary to offload read queries
# We'd partition the db by date or auction ids
# PostgreSQL can do tens of thousands of TPS per second but varies on the workload as well

from datetime import datetime, timedelta

class Auction:
    def __init__(self, expiry_date=None):
        self.bids = {}
        self.auction_deadline = (
            datetime.now() + timedelta(days=1) if expiry_date is None else expiry_date
        )
    
    def _is_before_deadline(self):
        return datetime.now() < self.auction_deadline

    def create_bid(self, user, amount):
        if self._is_before_deadline():
            self.bids[user] = amount
            self.marginal_price = 0.1
        else:
            print(f"No more bids, auction ended")

    def expire_bid(self, user):
        if self._is_before_deadline():
            expired_bid = self.bids.pop(user)
            print(f"Expiring bid for {user}({expired_bid})")
        else:
            print(f"No more changes, auction ended")

    def announce_winner(self):
        """Calculate winner for auction using 2nd price model"""
        sorted_bids = sorted(self.bids.items(), key=lambda item: item[1], reverse=True)
        n_largest = sorted_bids[:2]
        first, second = n_largest
        print(f"The winner is {first[0]}, paying {second[1]+self.marginal_price}")

    def __repr__(self):
        bidders_str = "Active Bids:\n"
        bidders_str += "\n".join([f"{user}: {amt}" for user, amt in self.bids.items()])
        return bidders_str

from flask import Flask
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Auction:
    uuid: str
    description: str
    expire_date: datetime
    reserve_price: float 
    status: str
    bids: int

@app.route('/auctions/<string:uuid>/bids/create', methods=['POST'])
def create_bid():
    return 

@app.route('/auctions/<string:uuid>/bids/expire', methods=['POST'])
def expire_bid():
    return 

@app.route('/auctions/<string:uuid>', methods=['GET'])
def announce():
    return 
