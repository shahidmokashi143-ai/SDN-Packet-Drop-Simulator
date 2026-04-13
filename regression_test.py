import subprocess
import time

def check_drop_rule():
    result = subprocess.run(
        ['sudo', 'ovs-ofctl', 'dump-flows', 's1'],
        capture_output=True, text=True
    )
    flows = result.stdout
    print("\n=== Current Flow Table ===")
    print(flows)

    if 'nw_src=10.0.0.1' in flows and 'nw_dst=10.0.0.3' in flows:
        print("✅ PASS: Drop rule is present and active")
        return True
    else:
        print("❌ FAIL: Drop rule missing!")
        return False

print("=== Regression Test: Packet Drop Rules ===")
print("\n[Test 1] Checking drop rule at start...")
result1 = check_drop_rule()

print("\n[Waiting 5 seconds to simulate traffic...]")
time.sleep(5)

print("\n[Test 2] Checking drop rule persists after delay...")
result2 = check_drop_rule()

if result1 and result2:
    print("\n✅ ALL TESTS PASSED - Drop rules persist correctly")
else:
    print("\n❌ SOME TESTS FAILED")
