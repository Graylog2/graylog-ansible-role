#!/usr/bin/bash
set -e
source $VIRTUAL_ENV/bin/activate

travis_retry()
{
  local result=0
  local count=1
  while [[ "${count}" -le 3 ]]; do
    [[ "${result}" -ne 0 ]] && {
      echo -e "\\n${ANSI_RED}The command \"${*}\" failed. Retrying, ${count} of 3.${ANSI_RESET}\\n" >&2
    }
    #run the command in a way that doesn't disable setting `errexit`
    "${@}"
    result="${?}"
    if [[ $result -eq 0 ]]; then break; fi
    count="$((count + 1))"
    sleep 1
  done

  [[ "${count}" -gt 3 ]] && {
    echo -e "\\n${ANSI_RED}The command \"${*}\" failed 3 times.${ANSI_RESET}\\n" >&2
  }

  return "${result}"
}


while sleep 9m; do echo "=====[ $SECONDS seconds still running ]====="; done &  #Bypass Travis CI's 10 minute timeout by printing to stdout every 9 minutes.
molecule create
kill %1  #Kill background sleep loop

travis_retry molecule converge
molecule verify
molecule destroy
