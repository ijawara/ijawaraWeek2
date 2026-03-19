from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_direction_too_high():
    # FIX: Regression test for swapped hint messages — "Too High" was saying "Go HIGHER!"
    # and "Too Low" was saying "Go LOWER!", sending the player in the wrong direction.
    # Claude Code caught this by tracing hint text against comparison logic.
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say go lower, got: {message}"

def test_hint_direction_too_low():
    # FIX: Mirrors the above — guess of 1 against secret of 50 should say go higher.
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say go higher, got: {message}"

def test_hard_range_is_larger_than_normal():
    # FIX: Regression test added with Claude Code to catch the Hard/Normal range swap bug.
    # Claude Code generated this test to verify Hard always has a wider range than Normal.
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard range (1-{hard_high}) should be larger than Normal range (1-{normal_high})"
    )
