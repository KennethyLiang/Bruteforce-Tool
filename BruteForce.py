import time  # Used to measure how long the brute-force attempt takes
import itertools  # For generating combinations more efficiently

def brute_force_pin_smart(correct_pin, max_length=None):
    """
    Smart brute force that tries shorter PINs first before longer ones.
    This is more realistic as most PINs are 4-6 digits.
    """
    start_time = time.time()
    total_attempts = 0
    
    # If max_length not specified, use the correct PIN's length as maximum
    if max_length is None:
        max_length = len(correct_pin)
    
    print(f"🎯 Target PIN: {correct_pin} ({len(correct_pin)} digits)")
    print(f"🔍 Searching PINs from 1 to {max_length} digits...")
    print("=" * 50)
    
    # Try each PIN length starting from 1 digit
    for current_length in range(1, max_length + 1):
        print(f"📊 Trying {current_length}-digit combinations...")
        
        # Generate all possible combinations for current length
        for guess in range(10 ** current_length):
            total_attempts += 1
            
            # Convert to string with leading zeros
            guess_str = str(guess).zfill(current_length)
            
            # Show progress every 10000 attempts for longer searches
            if total_attempts % 10000 == 0:
                elapsed = time.time() - start_time
                rate = total_attempts / elapsed if elapsed > 0 else 0
                print(f"  Progress: {total_attempts:,} attempts, {rate:.0f} attempts/sec")
            
            # Check if guess matches target
            if guess_str == correct_pin:
                elapsed = time.time() - start_time
                print(f"\n✅ PIN CRACKED!")
                print(f"🔑 Found PIN: {guess_str}")
                print(f"📈 Total attempts: {total_attempts:,}")
                print(f"⏱️ Time taken: {elapsed:.4f} seconds")
                print(f"🚀 Rate: {total_attempts/elapsed:.0f} attempts per second")
                return total_attempts
        
        print(f"  Completed all {10**current_length:,} combinations for {current_length} digits")
    
    print("❌ PIN not found within specified length range")
    return None

def brute_force_pin_exhaustive(correct_pin):
    """
    Traditional brute force that tries all combinations up to the PIN's length.
    More efficient if you know the exact PIN length.
    """
    pin_length = len(correct_pin)
    start_time = time.time()
    
    print(f"🎯 Target PIN: {correct_pin} ({pin_length} digits)")
    print(f"🔍 Exhaustive search through all {10**pin_length:,} combinations...")
    print("=" * 50)
    
    # Try all possible combinations of the known length
    for guess in range(10 ** pin_length):
        guess_str = str(guess).zfill(pin_length)
        
        # Show progress for longer searches
        if (guess + 1) % 25000 == 0:
            elapsed = time.time() - start_time
            progress = ((guess + 1) / (10 ** pin_length)) * 100
            rate = (guess + 1) / elapsed if elapsed > 0 else 0
            remaining_time = ((10 ** pin_length) - (guess + 1)) / rate if rate > 0 else 0
            print(f"Progress: {progress:.1f}% ({guess + 1:,}/{10**pin_length:,}) | "
                  f"Rate: {rate:.0f}/sec | ETA: {remaining_time:.1f}s")
        
        if guess_str == correct_pin:
            elapsed = time.time() - start_time
            print(f"\n✅ PIN CRACKED!")
            print(f"🔑 Found PIN: {guess_str}")
            print(f"📈 Attempts needed: {guess + 1:,}")
            print(f"⏱️ Time taken: {elapsed:.4f} seconds")
            print(f"🚀 Rate: {(guess + 1)/elapsed:.0f} attempts per second")
            return guess + 1
    
    print("❌ PIN not found")
    return None

def estimate_crack_time(pin_length):
    """
    Estimate how long it would take to crack a PIN of given length.
    """
    total_combinations = 10 ** pin_length
    # Assume average case: find PIN at 50% of search space
    avg_attempts = total_combinations // 2
    
    # Rough estimate: modern computer can try ~100,000 PINs per second
    estimated_rate = 100000  # attempts per second
    avg_time_seconds = avg_attempts / estimated_rate
    
    print(f"\n📊 CRACK TIME ESTIMATES for {pin_length}-digit PIN:")
    print(f"   Total combinations: {total_combinations:,}")
    print(f"   Average attempts needed: {avg_attempts:,}")
    print(f"   Worst case attempts: {total_combinations:,}")
    
    if avg_time_seconds < 1:
        print(f"   Average time: {avg_time_seconds*1000:.1f} milliseconds")
    elif avg_time_seconds < 60:
        print(f"   Average time: {avg_time_seconds:.1f} seconds")
    elif avg_time_seconds < 3600:
        print(f"   Average time: {avg_time_seconds/60:.1f} minutes")
    else:
        print(f"   Average time: {avg_time_seconds/3600:.1f} hours")

def main():
    print("🔓 Enhanced PIN Brute Force Tool")
    print("=" * 50)
    
    # Get PIN from user
    while True:
        pin = input("Enter a PIN to brute force (1-6 digits): ").strip()
        
        # Validate input
        if not pin.isdigit():
            print("⚠️ Please enter only digits (0-9)")
            continue
        elif len(pin) < 1 or len(pin) > 6:
            print("⚠️ Please enter a PIN between 1 and 6 digits long")
            continue
        else:
            break
    
    # Show crack time estimates
    estimate_crack_time(len(pin))
    
    # Ask user which method to use
    print(f"\nChoose brute force method:")
    print("1. Smart search (try shorter PINs first)")
    print("2. Exhaustive search (try all combinations of exact length)")
    print("3. Both methods (for comparison)")
    
    while True:
        choice = input("\nEnter choice (1, 2, or 3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("⚠️ Please enter 1, 2, or 3")
    
    print("\n" + "="*60)
    print("🚀 STARTING BRUTE FORCE ATTACK")
    print("="*60)
    
    if choice == '1':
        # Smart search
        brute_force_pin_smart(pin)
        
    elif choice == '2':
        # Exhaustive search
        brute_force_pin_exhaustive(pin)
        
    elif choice == '3':
        # Both methods for comparison
        print("\n🧠 METHOD 1: Smart Search")
        print("-" * 30)
        result1 = brute_force_pin_smart(pin)
        
        print(f"\n🔄 METHOD 2: Exhaustive Search")
        print("-" * 30)
        result2 = brute_force_pin_exhaustive(pin)
        
        # Compare results
        if result1 and result2:
            print(f"\n📊 COMPARISON:")
            print(f"   Smart search attempts: {result1:,}")
            print(f"   Exhaustive attempts: {result2:,}")
            if result1 < result2:
                improvement = ((result2 - result1) / result2) * 100
                print(f"   Smart search was {improvement:.1f}% more efficient!")
            elif result1 == result2:
                print("   Both methods took the same number of attempts")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ Brute force interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")