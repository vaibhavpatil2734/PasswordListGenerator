import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def delete_phase_data(phase_number):
    """
    Delete all files from a specific phase data folder.
    """

    data_folder = os.path.join(
        BASE_DIR,
        f"phase{phase_number}",
        f"phase{phase_number}Data"
    )

    if not os.path.exists(data_folder):
        print(f"⚠ Phase {phase_number} data folder not found.")
        return

    deleted_count = 0

    for file_name in os.listdir(data_folder):

        file_path = os.path.join(
            data_folder,
            file_name
        )

        if os.path.isfile(file_path):

            try:
                os.remove(file_path)

                print(f"✓ Deleted: {file_path}")

                deleted_count += 1

            except Exception as error:

                print(
                    f"✗ Could not delete "
                    f"{file_name}: {error}"
                )

    print(
        f"Phase {phase_number}: "
        f"{deleted_count} file(s) deleted."
    )


def reset():
    """
    Delete all phase data.
    """

    print("\nResetting all phase data...\n")

    for phase in range(1, 5):
        delete_phase_data(phase)

    print("\n✓ Reset completed.")
    print("✓ All phase data has been cleared.")


def keep_list():
    """
    Delete Phase 1, Phase 2 and Phase 3 data.
    Keep Phase 4 data.
    """

    print("\nKeeping Phase 4 list...\n")

    for phase in range(1, 4):
        delete_phase_data(phase)

    print("\n✓ Cleanup completed.")
    print("✓ Phase 1, 2 and 3 data cleared.")
    print("✓ Phase 4 data has been kept.")


def cleaner():

    print("\n============================================")
    print("              DATA MANAGEMENT")
    print("============================================")

    print("\n1. Reset")
    print("   Clear all Phase 1, 2, 3 and 4 data")

    print("\n2. Keep List")
    print("   Clear Phase 1, 2 and 3")
    print("   Keep Phase 4 data")

    print("\n3. Cancel")
    print("   Keep everything")

    print("\n============================================")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        reset()

    elif choice == "2":

        keep_list()

    elif choice == "3":

        print("\n✓ Nothing was deleted.")

    else:

        print("\n✗ Invalid choice.")
        print("Please select 1, 2 or 3.")


if __name__ == "__main__":
    cleaner()

