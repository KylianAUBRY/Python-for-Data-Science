def ft_tqdm(lst: range) -> None:
    """
    Simulate a progress bar for iterating through a range.

    Args:
        lst (range): The range to iterate through.

    Yields:
        Any: The current item from the range.
        is a keyword in Python used in the context of creating generators.
        Generators are a way to create iterators.
    """
    total = len(lst)
    progress_bar_width = 40
    len_t = len(str(total))

    for i, value in enumerate(lst, start=1):
        progress = i / total

        progress_info = f'{progress:>4.0%}'
        progress_size = progress * progress_bar_width

        progress_bar = f"{'█' * int(progress_size):<{progress_bar_width}}|"
        print(f"\r{progress_info}|{progress_bar} {i:>{len_t}}/{total}", end="")
        yield value
