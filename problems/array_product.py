if __name__ == "__main__":
    # get product array where each ith element is a product of elements of the array except the ith element
    # array of n integers
    inputArr = [1, 2, 3, 4]
    # product -> [24, 12, 8, 6]

    def getProduct(inputArr):
        n = len(inputArr)
        productArr = [1] * n

        leftProduct = 1
        for i in range(n):
            productArr[i] = leftProduct
            leftProduct *= inputArr[i]
            print(leftProduct)

        print(f"\nLeft Product: {productArr}\n")

        rightProduct = 1
        for i in range(n - 1, -1, -1):
            productArr[i] *= rightProduct
            rightProduct *= inputArr[i]

        print(productArr)

    getProduct(inputArr)
