

def find_remaining_pages(mystery_page_indices):

    n = 9
    count = 0
    page = 1

    while page <= 9:

        while page != mystery_page_indices[page-1]:

            count += 1
            page = mystery_page_indices[page-1]

        count += 1
        page += 1

    remaining = n - count
    print(remaining)






mystery_page_indices = [1, 3, 3, 6, 7, 8, 8, 8, 9]
find_remaining_pages(mystery_page_indices)