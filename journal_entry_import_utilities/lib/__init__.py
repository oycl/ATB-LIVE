def unlink_attachments(rec):
    """Clear attachments for the passed name."""
    rec.env["ir.attachment"].search([[
        "res_model", "=", rec._name
    ]]).unlink()