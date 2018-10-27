pragma solidity ^0.4.24;

contract DappStore{
    event Sign(address app, string name, string category, string homepage, string icon, string blockchain);
    event StageUpdate(address app, string name, string stage);
    //string[] states = ["protoype", "mvp", "alpha", "beta", "live"];

    function SignUp(string name, string category, string homepage, string icon, string blockchain) public {
        emit Sign(msg.sender, name, category, homepage, icon, blockchain);
        emit StageUpdate(msg.sender, name, "prototype");
    }

    function Update(string name, string stage) public {
        emit StageUpdate(msg.sender, name, stage);
    }
}