# Clip 2. alias 및 실행 모드 설정하기

## 목표

| 항목 | 내용 |
|---|---|
| 목적 | Claude Code를 짧은 명령으로 실행하고, 각 실행 모드를 구분한다 |
| 설정 대상 | `cc`, `ccd`, `ccr` |
| 원칙 | 수강생이 직접 설정하고 확인한다 |

## alias 목록과 실행 모드

| alias | 실제 명령 | 모드 | 용도 |
|---|---|---|---|
| `cc` | `claude` | 기본 모드 | Claude Code를 일반 실행한다 |
| `ccd` | `claude --dangerously-skip-permissions` | 빠른 실습 모드 | 권한 확인을 줄이고 실습 흐름을 빠르게 이어간다 |
| `ccr` | `claude --resume --dangerously-skip-permissions` | 이어하기 실습 모드 | 이전 세션을 이어서 빠르게 작업한다 |

## 핵심 포인트

| 포인트 | 설명 |
|---|---|
| `cc` | 평소에 가장 안전하게 쓰는 기본 실행 |
| `ccd` | 오늘처럼 파일 생성·수정·명령 실행을 반복할 때 쓰는 실습용 실행 |
| `ccr` | 앞에서 하던 Claude Code 대화를 이어서 다시 시작할 때 쓰는 실행 |
| 주의 | 빠른 실습 모드를 쓸수록 hook 같은 안전장치를 같이 설명한다 |

## 수강생 입력 프롬프트

```text
내 터미널이 zsh, bash, powershell 중 무엇인지 확인하고,
아래 Claude Code alias를 현재 터미널에 맞게 설정하는 방법을 안내해줘.

cc = claude
ccd = claude --dangerously-skip-permissions
ccr = claude --resume --dangerously-skip-permissions

설정 파일을 수정하기 전에 어떤 파일을 바꿀지 설명하고,
수정 후 새 터미널에서 확인하는 방법까지 알려줘.
```

## 터미널별 안내 포인트

| 터미널 | 설정 방식 |
|---|---|
| zsh | `~/.zshrc`에 alias 추가 |
| bash | `~/.bashrc` 또는 `~/.bash_profile`에 alias 추가 |
| PowerShell | 인자가 있는 alias는 `Set-Alias`가 아니라 function으로 설정 |

## 확인 프롬프트

```text
방금 설정한 alias가 정상 동작하는지 확인하고 싶어.
cc, ccd, ccr 각각 어떤 명령으로 확인하면 되는지 알려줘.
```

## 완료 기준

| 항목 | 확인 |
|---|---|
| `cc` 기본 모드를 이해했다 |  |
| `ccd` 빠른 실습 모드를 이해했다 |  |
| `ccr` 이어하기 실습 모드를 이해했다 |  |
| 본인 터미널에서 설정 파일 위치를 확인했다 |  |
