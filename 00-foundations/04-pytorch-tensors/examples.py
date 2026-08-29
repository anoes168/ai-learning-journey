import torch


def main():
    numbers = torch.arange(0, 10, 2)
    print("间隔为2：", numbers)

    matrix = torch.arange(12).reshape(3, 4)
    print("3行4列：")
    print(matrix)
    print("shape：", matrix.shape)


if __name__ == "__main__":
    main()
