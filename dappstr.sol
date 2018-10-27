pragma solidity ^0.4.24;

contract DappStore{
    event Sign(address app, string name, string category, string homepage, string icon);
    event StageUpdate(address app, string stage);
    //string[] states = ["protoype", "mvp", "alpha", "beta", "live"];

    function SignUp(string name, string category, string homepage, string icon) public {
        emit Sign(msg.sender, name, category, homepage, icon);
        emit StageUpdate(msg.sender, "prototype");
    }

    function Update(string stage) public {
        emit StageUpdate(msg.sender, stage);
    }
}