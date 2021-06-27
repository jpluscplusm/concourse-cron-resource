# Cron resource

A datetime-based [resource type](https://concourse-ci.org/implementing-resource-types.html) that understands cron syntax and emits regular new versions into a Concourse pipeline.

## Example

```yaml
---
resource_types:
- name: cron-resource
  type: docker-image
  source:
    repository: jpluscplusm/concourse-cron-resource

resources:
  - name: 10-min-trigger
    type: cron-resource
    source:
      expression: "*/10 * * * *"
```

## Source configuration

A `source` block configuring this resource contains the following keys:

- `expression`: a string containing a 5- or 6- field [cron](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression.

## Notes

FIXME:

- The period of per-resource or Concourse-wide checker interval can be unintuitive: "`check_every` simply sets a lower bound on the time between checks" (https://concourse-ci.org/checker.html#when-are-resources-checked). Document if/that we emit a version for each tick that the cron schedule implies, thus a longer `check_every` *could* result in multiple new versions when combined with a high-frequency schedule. The consumer should be careful to consume `latest` versus `every` version.
- Timezones
- Extended cron syntax, or not.
