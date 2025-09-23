#!/usr/bin/env python3
"""
Test script - GitHub stars yangilashini sinash uchun
"""

import subprocess
import sys
import os

def test_update():
    """GitHub stars yangilashini test qilish"""
    print("🧪 Testing GitHub Stars Update...")
    
    # Script mavjudligini tekshirish
    script_path = "scripts/update_stars.py"
    if not os.path.exists(script_path):
        print(f"❌ Script not found: {script_path}")
        return False
    
    try:
        # Python scriptni ishga tushirish
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=300)
        
        print("📤 Script Output:")
        print(result.stdout)
        
        if result.stderr:
            print("⚠️ Script Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ Test completed successfully!")
            return True
        else:
            print(f"❌ Test failed with return code: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Test timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

if __name__ == "__main__":
    success = test_update()
    sys.exit(0 if success else 1)
