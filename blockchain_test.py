from blockchain import Blockchain

bc = Blockchain()

bi_1 = bc.new_transaction('Dejan', 'Marija', 12)
print("Current Transactions:", bc.current_transactions)
print("Block index:", bi_1)
print("Blockchain:", bc.chain)

# input()

pw_1 = bc.proof_of_work(0)
print("Proof of Work 1:", pw_1)
print("Previous Hash for Block 1:", bc.chain[0]['previous_hash'])
nb_1 = bc.new_block(pw_1) # bc.chain[0]['previous_hash']
print("New block 1:", nb_1)
print("Blockchain:", bc.chain)

# input()

bi_2 = bc.new_transaction('Marija', 'Veljko', 6)
print("Current Transactions:", bc.current_transactions)
print("Block index:", bi_2)
print("Blockchain:", bc.chain)

# input()

pw_2 = bc.proof_of_work(pw_1)
print("Proof of Work 2:", pw_2)
print("Previous Hash for Block 2:", nb_1['previous_hash'])
nb_2 = bc.new_block(pw_2) # nb_1['previous_hash']
print("New block 2:", nb_2)
print("Blockchain:", bc.chain)

# input()

bi_3 = bc.new_transaction('Veljko', 'Dejan', 36)
print("Current Transactions:", bc.current_transactions)
print("Block index:", bi_3)
print("Blockchain:", bc.chain)

# input()

pw_3 = bc.proof_of_work(pw_2)
print("Proof of Work 3:", pw_3)
print("Previous Hash for Block 3:", nb_2['previous_hash'])
nb_3 = bc.new_block(pw_2) # nb_2['previous_hash']
print("New block 3:", nb_3)
print("Blockchain:", bc.chain)
