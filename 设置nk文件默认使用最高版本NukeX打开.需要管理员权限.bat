@ECHO off
CHCP 936
SETLOCAL ENABLEDELAYEDEXPANSION

SET "NUKE_DOWNLOAD_URL=http://thefoundry.s3.amazonaws.com/products/nuke/releases/10.5v7/Nuke10.5v7-win-x86-release-64.zip"

FOR %%i IN (
    11.1,
    11.0,
    10.5,
    10.0,
    9.0,
    8.0,
    7.0,
    6.0,
    ) DO (
    FOR %%j IN (10,9,8,7,6,5,4,3,2,1) DO (
        SET "NUKE_VERSION=%%iv%%j"
        SET "NUKE_INSTALL_PATH=C:\Program Files\Nuke!NUKE_VERSION!"
        ECHO Ѱ��Nuke!NUKE_VERSION!
        IF EXIST "!NUKE_INSTALL_PATH!" (
            ECHO �ҵ�Nuke!NUKE_VERSION!��
            GOTO install
        )
        ECHO ...
    )
)

REM Notify version mismatch.
ECHO.
ECHO.
ECHO δ�ڱ����Ϸ���֧�ֵ�Nuke�汾
ECHO ���ȷ�Ѱ�װ�� ����ϵ���������ļ�����
ECHO .
ECHO ��Nuke10.5v7������ַ...
explorer.exe "%NUKE_DOWNLOAD_URL%"
PAUSE
GOTO :EOF


:install

SET "NUKE_MAIN_VERSION=%NUKE_VERSION:~0,-2%"

ASSOC .nk=NukeScript
FTYPE NukeScript="C:\Program Files\Nuke%NUKE_VERSION%\Nuke%NUKE_MAIN_VERSION%.exe" --nukex "%%1"
ASSOC .hrox=NukeStudioProject
FTYPE NukeStudioProject="C:\Program Files\Nuke%NUKE_VERSION%\Nuke%NUKE_MAIN_VERSION%.exe" --studio "%%1"

PAUSE