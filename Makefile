list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | grep -E -v -e '^[^[:alnum:]]' -e '^$@$$'

init:
	poetry install --sync
	pre-commit install

style:
	pre-commit run ruff-format -a

lint:
	pre-commit run ruff -a

mypy:
	dmypy run sealens

deps:
	pre-commit run poetry-lock -a
	pre-commit run poetry-export -a

serve:
	python -mpanel serve app*.py --dev --address=127.0.0.1 --port=5009 --allow-websocket-origin=127.0.0.1:5009 --log-level debug
