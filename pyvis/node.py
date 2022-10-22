class Node(object):

    def __init__(self, n_id, shape, damage, reproducibility, exploitability, affected_users, discoverability, label, font_color=False, **opts):
        self.options = opts
        self.options["id"] = n_id
        self.options["label"] = label
        self.options["shape"] = shape
        self.options["damage"] = damage
        self.options["reproducibility"] = reproducibility
        self.options["exploitability"] = exploitability
        self.options["affected_users"] = affected_users
        self.options["discoverability"] = discoverability

        if font_color:
            self.options["font"] = dict(color=font_color)
