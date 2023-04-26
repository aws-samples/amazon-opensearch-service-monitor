/*!
Deck JS - deck.clone
Copyright (c) 2011 Remi BARRAQUAND
Dual licensed under the MIT license and GPL license.
https://github.com/imakewebthings/deck.js/blob/master/MIT-license.txt
https://github.com/imakewebthings/deck.js/blob/master/GPL-license.txt
*/

/*
This module provides a support for cloning the deck.
*/

(function($, deck, undefined) {
    var $d = $(document);
    var clones = new Array();
        
    $.extend(true, $[deck].defaults, {	
        keys: {
            clone: 67 // c
        }
    });

    /*
	jQuery.deck('addClone')
	
	Create a clone of this window and add it to the clones list.
	*/
    $[deck]('extend', 'addClone', function() {
        clone = new DeckClone();
        clones.push(clone);
        return clone;
    });
        
    /*
        jQuery.deck('Init')
        */
    $d.bind('deck.init', function() {
        var opts = $[deck]('getOptions');
        var container = $[deck]('getContainer');
        
        /* Bind key events */
        $d.unbind('keydown.deckclone').bind('keydown.deckclone', function(e) {
            if (e.which === opts.keys.clone || $.inArray(e.which, opts.keys.clone) > -1) {
                $[deck]('addClone');
                e.preventDefault();
            }
        });
    })
    /* Update current slide number with each change event */
    .bind('deck.change', function(e, from, to) {
        var opts = $[deck]('getOptions');
        var slideTo = $[deck]('getSlide', to);
        var container = $[deck]('getContainer');
	
        $.each(clones, function(index, clone) {
           clone.deck('go', to);
        });
    });
    
    /*
        Simple Clone manager (must be improved, by for instance adding cloning
        option e.g. propagate change, etc.)
        */
    var DeckClone = function() {
        var clone = window.open(window.location);
        
        this.deck = function() {
            clone['$'].deck.apply(clone['$'], arguments)
        }
    }
})(jQuery, 'deck');