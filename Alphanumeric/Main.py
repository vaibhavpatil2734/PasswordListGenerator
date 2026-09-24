import sys
import time
import os
import msvcrt

from cleaner import reset, keep_list

from phase4.phase4 import phase4
from phase3.phase3 import phase3
from phase1.phase1 import phase1
from phase2.phase2 import phase2


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
DIM = "\033[2m"


# ============================================================
# TERMINAL
# ============================================================

def clear_screen():
    os.system("cls")


def enable_colors():
    """
    Enable ANSI colors on Windows terminal.
    """
    os.system("")


# ============================================================
# HEADER
# ============================================================

def print_header():

    print(CYAN + r"""
    █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗ ██╗ ██████╗
   ██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██║██╔════╝
   ███████║██║     ██████╔╝███████║███████║██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║██║
   ██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║██║
   ██║  ██║███████╗██║     ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║██║╚██████╗
   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝
    """ + RESET)

    print(GREEN + "        PASSWORD LIST GENERATOR" + RESET)
    print(DIM + "        Secure Data Processing Tool" + RESET)

    print(CYAN + "\n" + "═" * 58 + RESET)

    print(
        WHITE
        + "  Greater data generates greater possibilities."
        + RESET
    )

    print(CYAN + "═" * 58 + RESET)


# ============================================================
# MENU
# ============================================================

def cleaner_menu():

    options = [
        "RESET — Clear ALL phase data",
        "KEEP LIST — Clear Phase 1-3, keep Phase 4",
        "CANCEL — Keep everything"
    ]

    selected = 0

    while True:

        clear_screen()
        print_header()

        print("\n" + YELLOW + "  DATA MANAGEMENT" + RESET)
        print(DIM + "  Use ↑ ↓ to select • ENTER to confirm" + RESET)
        print()

        for index, option in enumerate(options):

            if index == selected:

                print(
                    GREEN
                    + "  ▶ "
                    + option
                    + RESET
                )

            else:

                print(
                    DIM
                    + "    "
                    + option
                    + RESET
                )

        print()

        key = msvcrt.getch()

        # Arrow keys on Windows
        if key == b'\xe0' or key == b'\x00':

            key = msvcrt.getch()

            # UP
            if key == b'H':
                selected -= 1

                if selected < 0:
                    selected = len(options) - 1

            # DOWN
            elif key == b'P':
                selected += 1

                if selected >= len(options):
                    selected = 0

        # ENTER
        elif key == b'\r':

            clear_screen()
            print_header()

            if selected == 0:

                print("\n" + RED + "  ⚠ RESET SELECTED" + RESET)
                print(
                    YELLOW
                    + "  Clearing Phase 1, 2, 3 and 4 data..."
                    + RESET
                )

                reset()

                input(
                    "\nPress ENTER to continue..."
                )

                return

            elif selected == 1:

                print("\n" + YELLOW + "  KEEP LIST SELECTED" + RESET)
                print(
                    CYAN
                    + "  Clearing Phase 1, 2 and 3..."
                    + RESET
                )

                keep_list()

                input(
                    "\nPress ENTER to continue..."
                )

                return

            elif selected == 2:

                print(
                    "\n"
                    + GREEN
                    + "  ✓ No data was deleted."
                    + RESET
                )

                input(
                    "\nPress ENTER to continue..."
                )

                return


# ============================================================
# PHASE LOADING
# ============================================================

def loading_bar(phase_name, function, phase_number):

    print("\n")
    print(
        CYAN
        + f"  [ PHASE {phase_number} ] "
        + WHITE
        + phase_name
        + RESET
    )

    print(CYAN + "  " + "─" * 54 + RESET)

    total = 40

    for i in range(total + 1):

        percent = int((i / total) * 100)

        filled = "█" * i
        empty = "░" * (total - i)

        sys.stdout.write(
            "\r  "
            + GREEN
            + f"[{filled}{empty}]"
            + RESET
            + f" {percent:3d}%"
        )

        sys.stdout.flush()

        time.sleep(0.02)

    print()

    # Execute actual phase
    function()

    print(
        GREEN
        + f"  ✓ Phase {phase_number} completed successfully"
        + RESET
    )


# ============================================================
# MAIN
# ============================================================

def main():

    enable_colors()

    clear_screen()

    print_header()

    time.sleep(1)

    # Cleaner menu
    cleaner_menu()

    start_time = time.time()

    clear_screen()

    print_header()

    print(
        "\n"
        + GREEN
        + "  INITIALIZING PASSWORD GENERATION..."
        + RESET
    )

    time.sleep(0.7)

    # ========================================================
    # PHASE 1
    # ========================================================

    loading_bar(
        "Gathering Target Data",
        phase1,
        1
    )

    # ========================================================
    # PHASE 2
    # ========================================================

    loading_bar(
        "Combination Generation",
        phase2,
        2
    )

    # ========================================================
    # PHASE 3
    # ========================================================

    loading_bar(
        "Substitution Generation",
        phase3,
        3
    )

    # ========================================================
    # PHASE 4
    # ========================================================

    loading_bar(
        "Final Password Generation",
        phase4,
        4
    )

    # ========================================================
    # COMPLETE
    # ========================================================

    elapsed_time = time.time() - start_time

    print("\n" + CYAN + "═" * 58 + RESET)

    print(
        GREEN
        + "                 ✓ COMPLETE"
        + RESET
    )

    print(CYAN + "═" * 58 + RESET)

    print(
        WHITE
        + f"\n  Overall Progress : "
        + GREEN
        + "100%"
        + RESET
    )

    print(
        WHITE
        + f"  Processing Time  : "
        + CYAN
        + f"{elapsed_time:.2f} seconds"
        + RESET
    )

    print(
        WHITE
        + "  Status            : "
        + GREEN
        + "SUCCESS"
        + RESET
    )

    print(CYAN + "\n" + "═" * 58 + RESET)

    print(
        DIM
        + "  Password List Generator | Processing Complete"
        + RESET
    )

    print(CYAN + "═" * 58 + RESET)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

