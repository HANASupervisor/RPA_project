@echo off
setlocal

REM ==== Git 저장소 루트 확인 ====
for /f "delims=" %%i in ('git rev-parse --show-toplevel 2^>nul') do set "REPO=%%i"
if not defined REPO (
  echo [ERROR] Git 저장소 안에서 실행해 주세요.
  exit /b 1
)

REM ==== 경로 설정 (.github 사용) ====
set "TPL=%REPO%\.github\.gitmessage.txt"
set "HOOKDIR=%REPO%\.githooks"
set "COMMITMSG=%HOOKDIR%\commit-msg"

echo [INFO] REPO     = %REPO%
echo [INFO] Template = %TPL%
echo [INFO] HooksDir = %HOOKDIR%

REM ==== 파일 존재 여부 확인 ====
if not exist "%TPL%" (
  echo [ERROR] 템플릿 파일 없음: %TPL%
  echo         .github\.gitmessage.txt 를 먼저 만들어 주세요.
  exit /b 1
)
if not exist "%COMMITMSG%" (
  echo [ERROR] 훅 파일 없음: %COMMITMSG%
  echo         .githooks\commit-msg 를 먼저 만들어 주세요.
  exit /b 1
)

REM ==== 훅 폴더 보장 ====
if not exist "%HOOKDIR%" mkdir "%HOOKDIR%"

REM ==== Git 설정(현재 저장소만) ====
git config commit.template "%TPL%"
git config core.hooksPath "%HOOKDIR%"

REM ==== 실행 권한(가능하면 부여) ====
where bash >nul 2>nul
if %ERRORLEVEL%==0 (
  bash -lc "chmod +x '%COMMITMSG%'"
)

echo.
echo [OK] 이 저장소에 커밋 템플릿과 훅을 적용했습니다.
echo  - 템플릿: %TPL%
echo  - 훅 경로: %HOOKDIR%
echo.
echo VS Code를 기본 에디터로:  git config core.editor "code -w"
echo.

endlocal
