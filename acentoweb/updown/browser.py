from contentratings.browser.basic import BasicUserRatingView


class UpDownView(BasicUserRatingView):
    """View for the up/down voting."""

    vocab_name = 'acentoweb.updown.updown_vocab'
