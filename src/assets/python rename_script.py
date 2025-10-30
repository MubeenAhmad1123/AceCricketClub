import os
import sys
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# REVERSED Mapping: hashed filenames -> original filenames
# This removes the hashes and restores original names
filename_mapping = {
    # Images - REVERSED (from hashed to original)
    "ace-DCm5bXsn.webp": "ace-DCm5bXsn.webp",  # Keep as is
    "ahmad_result-BP76JCIv.webp": "ahmad_result.webp",
    "amant-t-CpJQTQUl.webp": "amant-t.webp",
    "amant-CTNNULEh.webp": "amant.webp",
    "amir-t-DRlM455o.webp": "amir-t.webp",
    "amir-Cjh2TlnA.webp": "amir.webp",
    "aqib-t-vVpgFmgf.webp": "aqib-t.webp",
    "aqib-X_YNAxeC.webp": "aqib.webp",
    "azam-t-cRiKFxpc.webp": "azam-t.webp",
    "azam-xLMNrH61.webp": "azam.webp",
    "badge-byx51Ytp.png": "badge.png",
    "bilal_result-DWb2nUr-.webp": "bilal_result.webp",
    "bowling macine-Dk0xmvRC.webp": "bowling macine.webp",
    "bowling-practice-5dspm28m.webp": "bowling-practice.webp",
    "brand1.webp": "brand1.webp",
    "brand2.webp": "brand2.webp",
    "brand3.webp": "brand3.webp",
    "brand4.webp": "brand4.webp",
    "brand5.webp": "brand5.webp",
    "brand6.webp": "brand6.webp",
    "brand7.webp": "brand7.webp",
    "captain-of-year-qA6GrHmu.webp": "captain-of-year.webp",
    "coach-feedback-CcYa1UT5.webp": "coach-feedback.webp",
    "community-BX6mPCll.webp": "community.webp",
    "david-t-iE7CDHDH.webp": "david-t.webp",
    "david-_5NPOCQi.webp": "david.webp",
    "facility-tour-CsvXyN53.webp": "facility-tour.webp",
    "faisal_result-C2a9oHYg.webp": "faisal_result.webp",
    "faislabad-DpeWAflW.webp": "faislabad.webp",
    "farhan-t-D6JKD0kx.webp": "farhan-t.webp",
    "farhan-DKSKaxcQ.webp": "farhan.webp",
    "fatima-BS_N6-RI.webp": "fatima.webp",
    "fitness-center-L-a1jbK_.webp": "fitness-center.webp",
    "fitness-training-Bqdw26SF.webp": "fitness-training.webp",
    "hassan_result-Deo2mCHZ.webp": "hassan_result.webp",
    "imran_result-Co7e_KXf.webp": "imran_result.webp",
    "indoor-nets-DuJ9sZoF.jpg": "indoor-nets.jpg",
    "islambad-DOYiJRJr.webp": "islambad.webp",
    "karachi-kNuGGWLQ.webp": "karachi.webp",
    "kashif_result-Ds5JEnEp.webp": "kashif_result.webp",
    "main-DaNF6tSr.png": "main.png",
    "match-day-BV5E3EVq.webp": "match-day.webp",
    "multan-JO9hW4pN.webp": "multan.webp",
    "new-facility-CPYk3iqy.webp": "new-facility.webp",
    "outdoor-ground-NoTnMGIS.webp": "outdoor-ground.webp",
    "partnership-B_rUNOmJ.webp": "partnership.webp",
    "peshawar-VMKT4FTr.webp": "peshawar.webp",
    "player-loung-B9OfnQG5.webp": "player-loung.webp",
    "pre-session-training-TSi8VzR5.webp": "pre-session-training.webp",
    "punjab-CYfUPp1R.webp": "punjab.webp",
    "regional-championship-C6YJtfGf.webp": "regional-championship.webp",
    "rizwan-DqRlavYR.webp": "rizwan.webp",
    "royal-CNB0Aim6.webp": "royal.webp",
    "saim-t-Bjcwb5Ay.webp": "saim-t.webp",
    "saim-i7svVmD4.webp": "saim.webp",
    "sarah-DGNfxp6S.webp": "sarah.webp",
    "sidra-C3TaQSCN.webp": "sidra.webp",
    "target-B5CPZBsG.webp": "target.webp",
    "tariq_result-CSS3k3XS.webp": "tariq_result.webp",
    "team-building-DNRAXoyM.webp": "team-building.webp",
    "thunder-DUA_92H4.webp": "thunder.webp",
    "training-session-CZzP5iAp.webp": "training-session.webp",
    "trophy-Duw7W6GJ.webp": "trophy.webp",
    "user-Ctd-xxMb.webp": "user.webp",
    "usman_result-DViWS12j.webp": "usman_result.webp",
    "video-analysis-CtdziK-l.webp": "video-analysis.webp",
    "youth-academy-9vunoePt.webp": "youth-academy.webp",
}

def rename_assets_inplace():
    """
    Rename files directly in the same directory as the script.
    REVERSED: Removes hashes and restores original names.
    """
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    renamed_count = 0
    not_found = []
    skipped = []
    
    print(f"Starting REVERSE file renaming process...")
    print(f"Removing hashes and restoring original names...")
    print(f"Working Directory: {script_dir}")
    print("-" * 50)
    
    # Check if we're in the right directory by looking for some hashed files
    sample_files = ["ahmad_result-BP76JCIv.webp", "badge-byx51Ytp.png", "main-DaNF6tSr.png"]
    found_samples = sum(1 for f in sample_files if (script_dir / f).exists())
    
    if found_samples == 0:
        print("\n[WARNING] No hashed image files found in this directory!")
        print(f"Current directory: {script_dir}")
        print("\nThis script is designed to remove hashes from filenames.")
        print("Make sure the script is in the correct folder with hashed images.")
    
    for hashed_name, original_name in filename_mapping.items():
        # Skip if names are the same
        if hashed_name == original_name:
            skipped.append(hashed_name)
            continue
            
        source_path = script_dir / hashed_name
        dest_path = script_dir / original_name
        
        if source_path.exists():
            try:
                # Check if destination already exists
                if dest_path.exists():
                    print(f"[SKIP] Original already exists: {hashed_name}")
                    skipped.append(hashed_name)
                else:
                    source_path.rename(dest_path)
                    print(f"[OK] {hashed_name} -> {original_name}")
                    renamed_count += 1
            except Exception as e:
                print(f"[ERROR] {hashed_name}: {str(e)}")
        else:
            not_found.append(hashed_name)
            # Don't print every missing file to reduce clutter
    
    print("-" * 50)
    print(f"\nSummary:")
    print(f"  Successfully renamed: {renamed_count} files")
    print(f"  Already original name: {len(skipped)} files")
    print(f"  Not found: {len(not_found)} files")

if __name__ == "__main__":
    print("=" * 50)
    print("IMAGE RENAMER SCRIPT (REVERSE)")
    print("=" * 50)
    print("\nThis script will REMOVE HASHES from filenames")
    print("Example: ahmad_result-BP76JCIv.webp -> ahmad_result.webp")
    print("\nWARNING: This will rename files in place!")
    print("Make sure you have a backup if needed.\n")
    
    response = input("Continue? (yes/no): ").lower().strip()
    
    if response == "yes":
        rename_assets_inplace()
        print("\n[DONE] Process complete! All hashes removed.")
    else:
        print("\n[CANCELLED] Operation cancelled.")