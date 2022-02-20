# Sync protocol for DennisMUD

[![Tests](https://github.com/pmer/dennisync/actions/workflows/run-tests.yml/badge.svg)](https://github.com/pmer/dennisync/actions/workflows/run-tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/pmer/dennisync/badge.svg?branch=main)](https://coveralls.io/github/pmer/dennisync?branch=main)

### Running

Library tests can be run with:

```sh
make init
make test
```

### Design

Has a data model, I/O model, and concurrency model

- Data model is list of list of objects
  - Outer list has fixed length and id
    - Basically just the list of DB tables
  - Inner list has dynamic length and objects have ids and timestamps
- I/O model is assumed to be:
  - Bluetooth LE
  - Assume a continuous local scan
  - Make and receive bidirectional, peer-to-peer connections at every opportunity
  - Sync all data objects with last-write-wins
    - Concurrent user state changes mean that after a sync sweep we can still be out-of-sync, but
      it is okay
  - Messaging consists of back-and-forth sending of 100% of objects
  - Gossip to remain effective during scale to large numbers (e.g., 50) of microcontrollers in the
    same room
- Concurrency safety (to some definition of "safe")
  - E.g., concurrent syncs on a single device

### Questions

- How to deal with object deletions

### Bonus

- Can use (e.g., Merkle tree-like or rsync-like) diff algorithm to increase transmission rate

### Limitations

- A controller DB might enter into an inconsistent state while sync is in-progress and may stay
  that way if sync is interrupted
  - Probably the best we can get with RAM and radio constraints, and within a reasonable complexity
  - Noisy radio, long range radio, or overloaded CPU can irritate

### Requirements

- Syncable data objects must have ids, and they must not collide
  - Can be random or can be a millisecond creation timestamp
  - Preferably, this id would not be revealed to a player for security reasons
- Syncable data objects must have last-modified timestamps
- Controller logic MUST gracefully handle inconsistent state
  - References to objects that don't exist
    - E.g., player might be standing in a room that was never created (specifically, this DB never
      had it inserted)
    - Player is holding an object that "never existed"
  - Objects that are supposed to reference each other might not
  - Etc.
  - Any behavior is okay as long as it is not to crash
    - Inconsistent states can (most of the time, if no mutations on the broken resources take
      place) be fixed with a sync, i.e., by waiting
- Transport layer to deal with packet segmentation on small-packet BLE messages
- Secure connection?

### Judgement

- Correctness
- CPU, memory, and bandwidth consumption
  - Energy consumption
- Sync speed
  - 1:1
  - Room of 50

### Implementation / this repo

- Library-type design
- Abstract data model and I/O
- Unit tests
- Dummy program to test on real hardware
