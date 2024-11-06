// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    // Mapping to store the balance of each customer (address)
    mapping(address => uint256) private balances;

    // Event to log deposits
    event Deposit(address indexed accountHolder, uint256 amount);

    // Event to log withdrawals
    event Withdrawal(address indexed accountHolder, uint256 amount);

    // Deposit function to add money to a user's bank account
    function deposit() public payable {
        require(msg.value > 0, "You need to deposit some money!");
        balances[msg.sender] += msg.value;

        // Emit a deposit event
        emit Deposit(msg.sender, msg.value);
    }

    // Withdraw function to withdraw money from a user's bank account
    function withdraw(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance!");

        // Deduct the balance and transfer the money to the caller
        balances[msg.sender] -= _amount;
        payable(msg.sender).transfer(_amount);

        // Emit a withdrawal event
        emit Withdrawal(msg.sender, _amount);
    }

    // Function to check the balance of the caller
    function checkBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
