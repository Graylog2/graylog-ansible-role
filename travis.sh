#!/usr/bin/bash
source $VIRTUAL_ENV/bin/activate
set -x
set -e

retry()
{
  set +e
  local result=0
  local count=1
  local retry_max=3
  while [[ "${count}" -le "${retry_max}" ]]; do
    [[ "${result}" -ne 0 ]] && {
      echo -e "\\n${ANSI_RED}The command \"${*}\" failed. Retrying, ${count} of ${retry_max}.${ANSI_RESET}\\n" >&2
    }
    #run the command in a way that doesn't disable setting `errexit`
    "${@}"
    result="${?}"
    if [[ $result -eq 0 ]]; then break; fi
    count="$((count + 1))"
    sleep 1
  done

  [[ "${count}" -gt "${retry_max}" ]] && {
    echo -e "\\n${ANSI_RED}The command \"${*}\" failed ${retry_max} times.${ANSI_RESET}\\n" >&2
  }
  set -e
  return "${result}"
}


while sleep 9m; do echo "=====[ $SECONDS seconds still running ]====="; done &  #Bypass Travis CI's 10 minute timeout by printing to stdout every 9 minutes.
molecule --debug create
kill %1  #Kill background sleep loop

retry molecule converge
molecule verify
molecule destroy
