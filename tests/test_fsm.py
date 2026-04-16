import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from automata.fsm import EnemyFSM

def test_enemy_fsm():
    fsm = EnemyFSM()
    assert fsm.get_current_state() == "PATROL"
    
    # Test transitions
    fsm.compute_next_state(200, 100)  # distance < 250, should chase
    assert fsm.get_current_state() == "CHASE"
    
    fsm.compute_next_state(40, 100)  # distance < 50, should attack
    assert fsm.get_current_state() == "ATTACK"
    
    fsm.compute_next_state(80, 100)  # distance > 70, should chase
    assert fsm.get_current_state() == "CHASE"
    
    fsm.compute_next_state(350, 100)  # distance > 300, should patrol
    assert fsm.get_current_state() == "PATROL"
    
    # Test death
    fsm.compute_next_state(100, 0)
    assert fsm.get_current_state() == "DEAD"