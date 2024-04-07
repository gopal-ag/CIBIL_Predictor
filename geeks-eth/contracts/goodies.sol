// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract InfoStorage {
    // Event that logs the addition of new information
    event InfoAdded(uint indexed id, string info);

    struct Info {
        string data;
    }

    Info[] public infos;

    // Function to add information to the contract
    function addInfo(string memory _data) public {
        infos.push(Info(_data));
        emit InfoAdded(infos.length - 1, _data);
    }

    // Function to retrieve information from the contract
    function getInfo(uint _index) public view returns (string memory) {
        require(_index < infos.length, "Info index is out of bounds.");
        return infos[_index].data;
    }
}
