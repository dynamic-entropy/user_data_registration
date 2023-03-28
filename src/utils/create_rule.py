
def create_rule(client, dids, options, dry_run=False):

    rse_expression = options["dest_rse_expression"]
    lifetime = options["lifetime"] 
    copies = options["copies"]
    ask_approval = options["ask_approval"]

    if dry_run:
        print(f"A rule will be created on {dids} at {rse_expression} for { lifetime if lifetime else 'Infinity'}")
        return ["DryRun"]

    return client.add_replication_rule(
        dids=dids,
        copies=1,
        rse_expression=rse_expression,
        grouping="ALL",
        activity="User Subscriptions",
        priority=1,
        lifetime = lifetime
    )