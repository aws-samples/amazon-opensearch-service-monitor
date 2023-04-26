/*!
Deck JS - deck.svg.toc
Copyright (c) 2011 Remi BARRAQUAND
Dual licensed under the MIT license and GPL license.
https://github.com/imakewebthings/deck.js/blob/master/MIT-license.txt
https://github.com/imakewebthings/deck.js/blob/master/GPL-license.txt
*/

/*
This module provides a support for animated SVG to the deck so as to create 
animation like in most presentation solution e.g powerpoint, keynote, etc.
Slides can include svg documents which then can be animated using the Animator.
*/

(function($, deck, undefined) {
    var $d = $(document);
   
    /*
	Extends defaults/options.
	*/
    $.extend(true, $[deck].defaults, {
        classes: {
            placeholder: 'deck-svg',
            control: 'deck-svg-control'
        }
    });
    
    /*
        jQuery.deck('Init')
        */
    $d.bind('deck.init', function() {
        var opts = $[deck]('getOptions');
        var container = $[deck]('getContainer');

        /* Go through all slides */
        $.each($[deck]('getSlides'), function(i, $el) {
            var $slide = $[deck]('getSlide',i);
            
            if( $slide.has("object[type='deckjs/asvg']").length>0 ) {
                $slide.data('animators', new Array());
            }
            
            /* Find all the object of type deckjs/asvg */
            $slide.find("object[type='deckjs/asvg']").each(function(index) {
                var id = $(this)
                /* Load attributes and validate them */
                var attributes = loadObjectParams(this);
                if( !validateParams(attributes) ) {
                    throw "Error while initializing "+$(this).attr('id')+", please ensure you have settup the required parameters."
                    return false;
                }
                
                /* Add this animator to the list of animators of the current slide. */
                $slide.data('animators').push(attributes['animator']);
                
                /* Create aSVG placeholder */
                var aSVG = createaSVG(this, attributes);
                $(this).replaceWith(aSVG['placeholder']);
                
                // Finaly load the SVG data
                aSVG['canvas'].svg({
                    loadURL: attributes['src'],
                    onLoad: function(svg) {
                        // nothing to do here
                    },
                    settings: {
                        // no settings
                    }
                });
            });
        });
    })
    /* Update current slide number with each change event */
    .bind('deck.change', function(e, from, to) {
        var opts = $[deck]('getOptions');
        var $slideTo = $[deck]('getSlide', to);
        var $container = $[deck]('getContainer');
	
        /* Restart all animator in the slide */
        if( $.isArray($slideTo.data('animators')) ) {
            $.each($slideTo.data('animators'), function(index, animator){
               $(window).attr(animator).restart();
            });
        }
    }).bind('deck.animator.init', function(e, data) {
        $('#deck-svg-next').removeClass("disabled");
    });
    
    /*
        Load parameters from an Object element
        */
    function loadObjectParams(objectElement) {
        var attributes = {};
        $(objectElement).children("param").each(function(index){
            attributes[$(this).attr("name")] = $(this).attr("value");
        });
        return attributes;
    }
    
    /*
        Return true if default params are set.
        */
    function validateParams(params) {
        return params['src'] && params['width'] && params['height'] && params['animator'];
    }
    
    /*
        Create aSVG placeholder
        */
    function createaSVG(object, attributes) {
        var $canvas, $control, $next, $reload, $placeholder;
        
        /* Create svg canvas */
        $canvas = $("<div />").attr({
            'id':  $(object).attr('id')
        }).css({
            'height': attributes['height'],
            'width': attributes['width']
        }).click(function(e) {
            var animator = $(window).attr(attributes['animator']);
            if( animator.isCompleted() ) {
                animator.restart();
            } else {
                animator.next();
            }
        });
                
        /* Create canvas control */
        
        // next button
        $next = $("<a href=\"#\"></a>").attr({
            'id':'deck-svg-next', 
            'class':'deck-svg-button'
        }).click(function(e) {
            var animator = $(window).attr(attributes['animator']);
            animator.next();
            if( animator.isCompleted() ) {
                $(this).addClass("disabled");
            }
        });
                
        // reload button
        $reload = $("<a href=\"#\"></a>").attr({
            'id':'deck-svg-reload', 
            'class':'deck-svg-button'
        }).click(function(e) {
            $(window).attr(attributes['animator']).restart();
            $next.removeClass("disabled");
        });

        // append everything in a control panel
        $control = $("<div />")
            .addClass($[deck]('getOptions').classes.control)
            .append($reload,$next);

        /* Create placeholder i.e canvas + control */
        $placeholder = $("<div />").attr({
            'class': $(object).attr('class')
        }).addClass($[deck]('getOptions').classes.placeholder)
          .append($canvas)
          .append($control);
            
        return {placeholder:$placeholder, canvas:$canvas};
    }
})(jQuery, 'deck');