Pytbo: Python Telegram Bots made easy
=====================================

.. image:: https://img.shields.io/pypi/v/pytbo.svg
    :target: https://pypi.python.org/pypi/pytbo

Pytbo is a module aimed at simplifying the creation of `Telegram Bots <https://telegram.org/blog/bot-revolution>`_ using Python.

A minimum familiarity with Telegram Bots is required to use this library. Please take a look at the `introduction <https://core.telegram.org/bots>`_ and the `FAQ <https://core.telegram.org/bots/faq>`_ before starting.

Getting Started
---------------

To start working with Pytbo, you must have a Bot token.
If you don't know what we're talking about, read how to `create your first bot with BotFather <https://core.telegram.org/bots#6-botfather>`_.

This is a simple *echo* bot done with Pytbo that looks for updates every 5 seconds.

.. code-block:: python

    import pytbo
    import time

    # Bot Token received from Telegram
    BOT_TOKEN = "MY_BOT_TOKEN"
    # Polling interval in seconds
    INTERVAL  = 5

    # Create bot object
    bot = pytbo.BareBot(BOT_TOKEN)
    # Print bot information
    print("Bot ID......: %s" % (bot.id))
    print("Bot username: %s" % (bot.username))

    # Initialize offset
    offset = 0
    # Infinite polling loop
    while True:
        # Look for updates
        updates = bot.getUpdates(offset)
        # Handle them
        for u in updates:
            if u.message:
                if u.message.text:
                    # If the update contains a message
                    # that contains text, we reply to the
                    # sender with the same text.
                    bot.sendMessage(
                        u.message.chat.id,
                        u.message.text,
                        reply_to_message_id=u.message.message_id
                    )
            # Update offset to avoid receiving
            # the same update again
            offset = u.update_id + 1
        # Sleep
        time.sleep(INTERVAL)

Installation
------------

To install Pytbo, simply:

.. code-block:: bash

    $ pip install pytbo

Documentation
-------------

A proper documentation is not yet available, but it will be.
However, useful methods and classes are documented inside the source code.

Don't be afraid to have a look inside, sometimes is the best way to learn.

How to Contribute
-----------------

#. Fork this repository on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Send a pull request.

Aknowledgements
---------------

Thanks to `Kenneth Reitz <https://github.com/kennethreitz>`_ and to all the other developers of the `requests <https://github.com/kennethreitz/requests>`_ module, which is used inside Pytbo and also as a blueprint for this repository and documentation layout.
