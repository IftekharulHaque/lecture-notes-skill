# Intro to Software Testing — Week 4
*Lecture, October 2025*

## Overview
This lecture introduced the difference between verification and validation, then spent most of the time on test doubles (mocks, stubs, fakes) and when each is appropriate. It closed with a walkthrough of a flaky test the instructor had pulled from a real codebase.

## Key Topics
- **Verification vs. validation** — verification asks "did we build the thing right?"; validation asks "did we build the right thing?"
- **Test doubles** — umbrella term for stand-ins used in place of real dependencies during testing (mocks, stubs, fakes, spies)
- **Stub vs. mock** — a stub returns canned data; a mock additionally asserts that it was called in a specific way
- **Flaky tests** — tests that pass or fail nondeterministically, usually due to shared state, timing, or unmocked external calls

## Notes

### Verification vs. validation
The lecture opened by distinguishing verification ("does the software conform to its spec?") from validation ("does the software actually solve the user's problem?"). The instructor's running example: a login form that perfectly implements a broken spec is verified but not validated. Unit tests mostly live in the verification camp; user research and UAT live in validation.

### Test doubles
The bulk of the lecture covered the taxonomy of test doubles:
- **Dummy** — passed around to satisfy a parameter list but never actually used.
- **Stub** — provides canned answers to calls made during the test; doesn't respond to anything outside what's programmed.
- **Fake** — has a real, working implementation, just not suitable for production (e.g. an in-memory database instead of a real one).
- **Spy** — a stub that also records how it was called, so the test can inspect that later.
- **Mock** — pre-programmed with expectations about how it will be called, and the test fails if those expectations aren't met.

The instructor stressed that mocks should be used sparingly — over-mocking couples tests tightly to implementation details, so refactoring the implementation (without changing behavior) can break tests that shouldn't have cared.

### Case study: a flaky test
The instructor showed a real test from a payments service that failed roughly 1 in 20 runs. [unclear: the exact service name given was hard to make out, transcribed as something like "Ledger-something"]. The root cause was a stub returning `System.currentTimeMillis()` instead of a fixed clock, so tests occasionally straddled a millisecond boundary. Fix: inject a fake clock instead of stubbing time calls individually.

## To-Dos
- [ ] Read chapter 6 ("Test Doubles") before next class
- [ ] Refactor the `PaymentServiceTest` from the homework repo to use a fake clock instead of stubbing `System.currentTimeMillis()` — due next Monday
- [ ] Optional: bring one example of a flaky test from your own project to discuss next week
