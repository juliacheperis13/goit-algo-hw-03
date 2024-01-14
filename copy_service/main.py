from recursive_copy_service import RecursiveCopyService


def catch_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("File or directory is not found.")
        except KeyboardInterrupt:
            print("Thank you for using the copy service!")
        except:
            print("Something went wrong.")

    return inner


@catch_error
def run_copy():
    copy_service = RecursiveCopyService()
    copy_service.init()
    args = copy_service.parse_argv()
    copy_service.file_copy(args.source, args.dist)


def main():
    run_copy()

if __name__ == "__main__":
    main()
