# Bank - Python <!-- omit in toc -->

This is a small project to practice maintaining code quality and process. [Source]

I have previously created a Ruby implementation, [available here](https://github.com/hturnbull93/bank/).
I have also created a JavaScript implementation for the [browser](https://github.com/hturnbull93/bank-js/), and in [node](https://github.com/hturnbull93/bank-node/).

It allows you to create an account, deposit funds into it, withdraw funds from it, and print statements.

- [Spec](#spec)
  - [Requirements](#requirements)
  - [Acceptance criteria](#acceptance-criteria)
- [Quick Start](#quick-start)
- [Screen Preview](#screen-preview)
- [Dependencies](#dependencies)
- [Development Journal](#development-journal)
  - [Domain Modelling](#domain-modelling)
  - [User Stories](#user-stories)
  - [Set up](#set-up)
  - [Deposits](#deposits)
  - [Withdrawals](#withdrawals)
  - [Statement](#statement)
  - [Transactions](#transactions)
  - [Back to the Statement](#back-to-the-statement)
  - [Todo](#todo)

## Spec

### Requirements

- You should be able to interact with your code via a REPL like IRB or the JavaScript console. (You don't need to implement a command line interface that takes input from STDIN.)
- Deposits, withdrawal.
- Account statement (date, amount, balance) printing.
- Data can be kept in memory (it doesn't need to be stored to a database or anything).

### Acceptance criteria

**Given** a client makes a deposit of 1000 on 10-01-2012  
**And** a deposit of 2000 on 13-01-2012  
**And** a withdrawal of 500 on 14-01-2012  
**When** she prints her bank statement  
**Then** she would see:

```irb
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```

## Quick Start

Coming soon.

## Screen Preview

Coming soon.

## Dependencies

Development:

[pytest] - Testing framework.
[freezegun] - datetime module mock library.

## Development Journal

### Domain Modelling

Given that I know more about the final form of the program from the previous implementations, this project focusses more on the implementation rather than the planning steps. The below CRC modelling and User Stories are taken from the Ruby implementation.

CRC modelling:

![CRC Model](images/Bank-REPL-CRC.png)

### User Stories

- [x] 1

> As a Bank Manager,  
> So that we only take customers money,  
> I want accounts to start with balance 0

- [x] 2

> As a Customer,  
> So I can keep my money safe,  
> I want to be able to deposit into my account

- [x] 3

> As a Customer,  
> So I can spend my money,  
> I want to be able to withdraw from my account

- [x] 3.1

> As a Bank Manager,  
> So we don't go out of pocket,  
> I want withdrawals to only be allowed to occur if the customer has sufficient funds

- [ ] 4

> As a Customer,  
> So I can keep on top of my finances,  
> I want to be able to print my account statement

- [x] 4.1

> As a Customer,  
> So I know when each transaction happened,  
> I want transactions on my statement to have the date

- [x] 4.2

> As a Customer,  
> So I know how much each deposit was,  
> I want deposits on my statement to have the credit amount.

- [x] 4.3

> As a Customer,  
> So I know how much each withdrawal was,  
> I want withdrawals on my statement to have the debit amount.

- [ ] 4.4

> As a Customer,  
> So can keep track of my balance,  
> I want transactions on my statement to have the balance amount after the transaction was completed.

- [ ] 4.5

> As a Customer,  
> Because more recent transactions are more important to me,  
> I want the statement transactions to be ordered from newest to oldest.

### Set up

This is my first ever Python project.

I am using Python 3.8.3.

For my tests I am using pytest, installed with:

```shell
pip install -U pytest
```

### Deposits

- [x] 1

> As a Bank Manager,  
> So that we only take customers money,  
> I want accounts to start with balance 0

- [x] 2

> As a Customer,  
> So I can keep my money safe,  
> I want to be able to deposit into my account

In `test/account_test.py`:

Wrote a test for an `Account` class, with a `deposit` method taking 100 results in a string showing deposited 100 and balance of 100. Red.

In `lib/account.py`:

- Added a an `Account` class, that has a method `deposit`, taking self, and an amount, and returning the relevant string hardcoded.

Also added `__init__.py` files to each of the root fir, `lib`, and `test`, in order to allow `Account` to be imported into the test file from `lib.account`.

Green.

Wrote test for `deposit` method taking 200 results in a string showing deposited 200.00 and balance of 200.00. Red.

- `deposit` has a variable `message` defined as a string with placeholders.
- `deposit` returns `message` formatted passing in the amount.

Green.

Wrote test for `deposit` method taking 200 then 100 results in a string showing deposited 100.00 and balance of 300.00. Red.

- Add constant `STARTING_BALANCE` assigned with 0 to the class.
- Assign variable `balance` with `STARTING_BALANCE`.
- `deposit` adds the amount passed to the balance, then formats that amount and the balance into the string.

Green.

Wrote test for `deposit` method taking 10.50, should in a string showing deposited 10.50 and balance of 10.50. Red.

The balance should probably be stored as pence, rather than as a float, but it needs to be display at two decimal places as if it were pounds and pence.

- In `deposit` assign `credit` with the passed amount * 100, to express it as pence.
- add `credit` to the balance.
- `displayBalance` and `displayCredit` assigned with the balance and credit divided by 100 (to convert the pence figure to pounds and pence).
- Format string uses `:.2f` to convert to 2 decimal places.
- return the format string with the `displayBalance` and `displayCredit`.

Green.

Refactors:

- Extracted methods `pence` and `pounds` to handle conversion to and from pounds and pence.
- Moved these into their own module `money`.

### Withdrawals

- [x] 3

> As a Customer,  
> So I can spend my money,  
> I want to be able to withdraw from my account

Wrote test for withdrawing 100 from an account with 1000, returned string has balance: 900.00. Red.

- Add `withdraw` method returning a hardcoded string.

Green.

Wrote test for withdrawing 200 from an account with 1000, returned string has balance: 800.00. Red.

- `withdraw` checks if the amount is 200 and returns the relevant string, else returns the string from before.

Green.

Wrote test for withdrawing 200 then 100 from an account with 1000, returned string has balance: 700.00. Red.

`withdraw` implements similar functionality to `deposit` but deducting the amount from the balance.

- [x] 3.1

> As a Bank Manager,  
> So we don't go out of pocket,  
> I want withdrawals to only be allowed to occur if the customer has sufficient funds

Wrote test for withdrawing 1500 from an account with 1000, string returned should say "Insufficient funds". Red.

- Added guard clause to check if the amount to be withdrawn is greater than the current balance, if so return the string.

### Statement

- [ ] 4

> As a Customer,  
> So I can keep on top of my finances,  
> I want to be able to print my account statement

The feature test I want to write needs to be able to have the date mocked. For this I will use the [freezegun] library, installed with `pip install -U freezegun`.

In `test/account_feature_test.py` wrote a feature test similar to the above acceptance criteria, using freezegun to mock the date. Red.

To help solve the feature test I think I should implement `Transaction`s.

### Transactions

- [x] 4.1

> As a Customer,  
> So I know when each transaction happened,  
> I want transactions on my statement to have the date

In `test/transaction_test.py` wrote a test for the `display` method of the `Transaction` class to return a string with the formatted date in the first column. Red.

In `lib/transaction.py`:

- `Transaction` has a `DATE` constant set with the current date and time. It also has a `DATE_FORMAT` constant that is set with a formatted version of `DATE`.
- `display` is a method that has a variable `template` assigned with a format strig, and it returns the template with the `DATE_FORMAT` formatted into it.

Green.

Refactors:

- I realised I had not been using instance variables for things like `Account` `balance` and `Transaction` `DATE` etc. (My bad, I am new at python!). Added `__init__` methods to initialise new instances and set instance variables.

- [x] 4.2

> As a Customer,  
> So I know how much each deposit was,  
> I want deposits on my statement to have the credit amount.

Wrote a test for constructing a transaction instance with a credit value as a keyword argument, its `display` method should include that value in the second column of the returned string. Red.

- `__init__` takes the keyword argument credit defaulting to `None`, assigning this to `self.credit`.
- The method `format` takes self and `item`, then if `item` is not `None`,  it uses `pounds` imported from `money` to convert the item, then formats that as a 2 decimal place figure with a trailing space, else returns an empty string.
- `display` formats in the `format` of `self.credit` in column two.

Green.

- [x] 4.3

> As a Customer,  
> So I know how much each withdrawal was,  
> I want withdrawals on my statement to have the debit amount.

Wrote a test for constructing a transaction instance passing in debit value as keyword argument, its `display` method should include the debit value in the third column of the returned string. Red.

- `__init__` takes the keyword argument debit defaulting to `None`, assigning this to `self.debit`.
- In the third column of the template string, insert the `format` of `self.debit`.

Green.

- [ ] 4.4

> As a Customer,  
> So can keep track of my balance,  
> I want transactions on my statement to have the balance amount after the transaction was completed.

Wrote a test for constructing a transaction instance passing in balance value as keyword argument, its `display` method should include the balance value in the fourth column of the returned string. Red.

- `__init__` takes the keyword argument balance defaulting to `None`, assigning this to `self.balance`.
- In the fourth column of the template string, insert the `format` of `self.debit`.

Green.

Refactors:

- As the column delimiters are all " ||", switch to an list that is joined by that delimiter instead of a template string.
- Extract out the two decimal place formatting from format to the `money.pounds` function.
- Renamed `Transaction`'s `format` method to `render` to avoid confusion with the string method `format`.
- Renamed helper methods that should be private prepending two underscores to their name.

### Back to the Statement

The `Transaction` class can now be injected into the `Account` class.

Wrote a test that the `deposit` method should call for a new `Transaction` passing credit and balance.

- `Account.__init__` takes a keyword argument `transaction_class` defaulting to `Transaction`.
- `deposit` calls for a new `Transaction` instance passing in credit and balance.

Green.

Wrote a test that the `withdraw` method should call for a new `Transaction` passing debit and balance.

- `withdraw` calls for a new `Transaction` instance passing in debit and balance.

Green.

Refactors:

- As the behaviour in `deposit` and `withdraw` is similar, extracted a private helper method `__add_transaction`, which `deposit` and `withdraw` call.

Passing the feature test:

- In `Account`'s `__init__` method, assign `self.TRANSACTION_HISTORY` as an empty list.
- In `__add_transaction`, append the created transaction onto the `TRANSACTION_HISTORY`.
- The `statement` creates a copy of `self.TRANSACTION_HISTORY` in the constant `REVERSE_TRANSACTIONS`, which is then reverses.
- A nested function `mapping` takes a transaction and calls `display` on it.
- `MAPPED_ROWS` is assigned with the map of `mapping` and `REVERSE_TRANSACTIONS`.
- Then `JOINED_ROWS` is assigned with a `SEPARATOR` ("\n") joining the `MAPPED_ROWS`.
- Finally, it returns `self.STATEMENT_HEADER` (a string with the titles for the columns) concatenated with `JOINED_ROWS`.

Refactors: 

- Extracted a `__reverse_transactions` method to copy and reverse the transactions.
### Todo

- [ ] Extract printer class.
- [ ] See if it is best practice to define anything that isn't intended to change as a CONSTANT.
- [ ] Get it actually working in a REPL.
- [ ] Do the mock dependency injection properly when I have more time.

<!-- links -->

[pytest]: https://docs.pytest.org/en/latest/
[freezegun]: https://github.com/spulec/freezegun/