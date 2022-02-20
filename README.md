# Sync protocol for DennisMUD

### Design

- Abstract data and I/O models to ease integration
- Data model is list of list of objects
    - Outer list has fixed length and id
    - Inner list has dynamic length and objects have ids and timestamps
- I/O model is assumed to be:
  - Bluetooth LE
  - Assume a continuous local scan
  - Make and receive bidirectional, peer-to-peer connections at every opportunity
  - Sync all data objects with last-write-wins
    - Concurrent user state changes mean that after a sync sweep we can still be out-of-sync, but it is okay
  - Messaging consists of back-and-forth sending of 100% of objects
  - Gossip to remain effective during scale to large numbers (e.g., 50) of microcontrollers in the same room
- Concurrency safe (to some definition of "safe")

### Questions

- How to deal with object deletions

### Bonus

- Can use (e.g., Merkle tree-like or rsync-like) diff algorithm to increase transmission rate

### Limitations

- A controller DB might enter into an inconsistent state while sync is in-progress and may stay that way if sync is
  interrupted
  - Could get better results if we had large RAM, and would be less likely if we used higher-bandwidth radio
  - Noisy radio background / long range can irritate

### Requirements

- Syncable data objects must have ids, and they must be random and not collide
- Syncable data objects must have last-modified timestamps
- Controller logic MUST gracefully handle inconsistent state
  - References to objects that don't exist
  - Objects that are supposed to reference each other might not
    - E.g., player might be standing in a room that was never created (specifically, this DB never had it inserted)
  - Etc.
- Needs a transport layer to deal with packet segmentation on small-packet BLE messages

### Judgement

- Correctness
- CPU speed, memory consumption, network bandwidth consumption
  - Energy consumption
- Sync speed
