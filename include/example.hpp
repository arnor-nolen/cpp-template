#ifndef EXAMPLE_HPP
#define EXAMPLE_HPP

class Example {
  public:
    explicit Example();
    ~Example() = default;

    Example(const Example &) = delete;
    Example(Example &&) noexcept = delete;

    auto operator=(const Example &) -> Example & = delete;
    auto operator=(Example &&) noexcept -> Example & = delete;
};

#endif
