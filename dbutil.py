from app.core.database import DatabaseManager
import argparse
import sys

dbmanager = DatabaseManager()

def list_datasets():
    """List the names of all datasets."""
    metadata = dbmanager.get_all_generate_metadata()
    if metadata:
        col_widths = {
            "id": max(len("ID"), max(len(str(d["id"])) for d in metadata)),
            "display_name": max(len("Display Name"), max(len(str(d["display_name"])) for d in metadata)),
            "file_name":    max(len("File Name"),    max(len(str(d["generate_file_name"])) for d in metadata)),
            "created_date": max(len("Created Date"), max(len(str(d["timestamp"])) for d in metadata)),
        }
    
        header = (
            f"{'ID':<{col_widths['id']}}  "
            f"{'Display Name':<{col_widths['display_name']}}  "
            f"{'File Name':<{col_widths['file_name']}}  "
            f"{'Created Date':<{col_widths['created_date']}}"
        )
        separator = "  ".join("=" * w for w in col_widths.values())
    
        print(header)
        print(separator)
        for data in metadata:
            print(
                f"{str(data['id']):<{col_widths['id']}}  "
                f"{str(data['display_name']):<{col_widths['display_name']}}  "
                f"{str(data['generate_file_name']):<{col_widths['file_name']}}  "
                f"{str(data['timestamp']):<{col_widths['created_date']}}"
        )
    else:
        print("No dataset found")


def delete_dataset(id: str):
    """Delete a dataset by name."""
    print(f"Deleting dataset: '{id}' ...")
    dbmanager.delete_generate_data(file_name=None, id=id)
    print(f"  Dataset '{id}' deleted successfully.")


def list_evaluations():
    """List the names of all evaluations."""
    metadata = dbmanager.get_all_evaluate_metadata()
    if metadata:
        col_widths = {
            "id": max(len("ID"), max(len(str(d["id"])) for d in metadata)),
            "display_name": max(len("Display Name"), max(len(str(d["display_name"])) for d in metadata)),
            "file_name":    max(len("File Name"),    max(len(str(d["evaluate_file_name"])) for d in metadata)),
            "created_date": max(len("Created Date"), max(len(str(d["timestamp"])) for d in metadata)),
        }
    
        header = (
            f"{'ID':<{col_widths['id']}}  "
            f"{'Display Name':<{col_widths['display_name']}}  "
            f"{'File Name':<{col_widths['file_name']}}  "
            f"{'Created Date':<{col_widths['created_date']}}"
        )
        separator = "  ".join("=" * w for w in col_widths.values())
    
        print(header)
        print(separator)
        for data in metadata:
            print(
                f"{str(data['id']):<{col_widths['id']}}  "
                f"{str(data['display_name']):<{col_widths['display_name']}}  "
                f"{str(data['evaluate_file_name']):<{col_widths['file_name']}}  "
                f"{str(data['timestamp']):<{col_widths['created_date']}}")
    else:
        print("No evaluations found")


def delete_evaluation(id: str):
    """Delete an evaluation by ID."""
    print(f"Deleting evaluation: '{id}' ...")
    dbmanager.delete_evaluate_data(file_name=None, id=id)
    print(f"  Evaluation '{id}' deleted successfully.")


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dbutil",
        description="Manage datasets and evaluations from the command line.",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")
    subparsers.required = True

    # list_datasets
    subparsers.add_parser(
        "list_datasets",
        help="List the names of all datasets.",
    )

    # delete_dataset
    p_del_ds = subparsers.add_parser(
        "delete_dataset",
        help="Delete a dataset by ID.",
    )
    p_del_ds.add_argument(
        "id",
        help="ID of the dataset to delete.",
    )

    # list_evaluations
    subparsers.add_parser(
        "list_evaluations",
        help="List the names of all evaluations.",
    )

    # delete_evaluation
    p_del_ev = subparsers.add_parser(
        "delete_evaluation",
        help="Delete an evaluation by ID.",
    )
    p_del_ev.add_argument(
        "id",
        help="ID of the evaluation to delete.",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list_datasets":
        list_datasets()
    elif args.command == "delete_dataset":
        delete_dataset(args.id)
    elif args.command == "list_evaluations":
        list_evaluations()
    elif args.command == "delete_evaluation":
        delete_evaluation(args.id)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()