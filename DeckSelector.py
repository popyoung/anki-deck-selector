# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/popyoung/anki-deck-selector

from aqt import mw, gui_hooks

def keyEvent(self):
    mw.web.eval("""
    document.querySelector('.current').scrollIntoView({block: "nearest"});
    document.addEventListener('keydown', function(event) {
        var current = document.querySelector('.current');
        if (event.key === 'ArrowUp') {
            var prev = current.previousElementSibling;
            if (prev&&!prev.classList.contains("top-level-drag-row")) {
                current.classList.remove('current');
                prev.classList.add('current');
                pycmd('select:'+prev.id);
            }
            document.querySelector('.current').scrollIntoView({block: "nearest"});
            event.preventDefault();
        } else if (event.key === 'ArrowDown') {
            var next = current.nextElementSibling;
            if (next) {
                current.classList.remove('current');
                next.classList.add('current');
                pycmd('select:'+next.id);
            }
            document.querySelector('.current').scrollIntoView({block: "nearest"});
            event.preventDefault();
        }
        
    });
    """)

gui_hooks.deck_browser_did_render.append(keyEvent)