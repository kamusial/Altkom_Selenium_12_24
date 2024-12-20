*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wiki login}       RobotTests
${wiki password}    RobotFramework
${wrong wiki password}   1234
${wrong_message}   Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.

*** Keywords ***

*** Test Cases ***
Successful Log in Wikipedia
    Open Browser    https://pl.wikipedia.org    chrome
    Maximize Browser Window
    Click element   pt-login-2
    Sleep    3
    input text   wpName   ${wiki login}
    Sleep    1
    input text   wpPassword1   ${wiki password}
    Sleep    1
    Select Checkbox   wpRemember
    Sleep    1
    click button    id:wpLoginAttempt
    Sleep    3
    Close Browser

NonSuccessful Log in Wikipedia
    Open Browser    https://pl.wikipedia.org    chrome
    Click element   pt-login-2
    Sleep    3
    input text   wpName   ${wiki login}
    Sleep    1
    input text   wpPassword1   ${wrong wiki password}
    Sleep    1
    Select Checkbox   wpRemember
    Sleep    1
    click button    id:wpLoginAttempt
    Sleep    3


    #userloginForm > form > div.cdx-message.cdx-message--block.cdx-message--error > div
    ${my_message}   get text    //*[@id="userloginForm"]/form/div[1]/div
    log    ${my_message}
    log to console    ${my_message}
    Sleep    3
    Close Browser
