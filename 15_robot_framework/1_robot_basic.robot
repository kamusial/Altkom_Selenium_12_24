*** Settings ***
Library    SeleniumLibrary
Test Setup   Open Browser    https://pl.wikipedia.org    chrome
Test Teardown   Close Browser

*** Variables ***
${wiki login}       RobotTests
${wiki password}    RobotFramework
${wrong wiki password}   1234
${wrong_message}   Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz

*** Keywords ***
Log in Wikipedia
    [Arguments]    ${login}    ${password}
    Maximize Browser Window
    Wait Until Element Is Visible   id:pt-login-2   3
    Click element   id:pt-login-2
    input text   name:wpName   ${login}
    input password   wpPassword1   ${password}
    Run Keyword And Ignore Error   Select Checkbox   wpRemember
    click button    id:wpLoginAttempt

*** Test Cases ***
Successful Log in Wikipedia
    Log in Wikipedia   ${wiki login}   ${wiki password}


NonSuccessful Log in Wikipedia
    Log in Wikipedia    ${wiki login}    ${wrong wiki password}
    ${my_message}   get text    //*[@id="userloginForm"]/form/div[1]/div
    log    ${my_message}
    log to console    ${my_message}
    Should Be Equal As Strings   ${my_message}   ${wrong_message}

