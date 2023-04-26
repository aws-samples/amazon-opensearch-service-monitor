/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

function Animator(target, animations) {
    
    var anims,  // list of all animations
    cursor,     // pointer to the current animation
    
    events = {
		/*
		This event fires whenever the current animation is completed.
                The callback function is passed one parameter, target, equal to 
                the target on which the animation completed.
		
		$(document).bind('deck.animator.completed', function(target) {
		   alert('The animation of '+target+' has just completed.');
		});
		*/
		completed: 'deck.animator.completed',
		
                /*
		This event fires whenever an animation is performed. The callback
                function is passed two parameters, target and index, equal to
                the target on which the animation is performed and the index of
                the animation i.e between 0 and animation.lenght.
		*/
		progress: 'deck.animator.progress',
                
		/*
		This event fires at the beginning of deck.animator initialization.
		*/
		beforeInitialize: 'deck.animator.beforeInit',
		
		/*
		This event fires at the end of deck.animator initialization.
		*/
		initialize: 'deck.animator.init' 
	};
    
    if( $.isArray(animations) ) {
        anims = animations;
        cursor = 0;
    } else {
        throw "Animator only takes an array of animation as argument.";
    }
    
    /*
        Restart animator.
        */
    this.restart = function() {
        init();
    }

    /*  
        Move to next animation.
        */
    this.next = function() {
        if( cursor < anims.length ) {
            anim = animations[cursor++];
            if( $.isArray(anim) ) {
                $(anim).each( function() {
                    this(target);
                });
            } else {
                anim(target);
            }
            $(document).trigger(events.progress, {'target':target, 'index':cursor-1});
        } else {
            $(document).trigger(events.completed, {'target':target});
        }
    }
   
    /*  
        Return true if animation is complete.
        */
    this.isCompleted = function() {
        return cursor == anims.length;
    }
    
    /*
        Push new animation into the animator.
        */
    this.push = function(anim) {
        this.anims.push(anim);
    }
    
    function init() {            
        $(document).trigger(events.beforeInitialize, {'target':target});
        
        cursor = 0;
        if( anims.length>0 ) {
            anim = animations[cursor++];
            if( $.isArray(anim) ) {
                $(anim).each( function() {
                    this(target);
                });
            } else {
                anim(target);
            }
            
            $(document).trigger(events.initialize, {'target':target});   
        } else {
            throw "Animator requires at list one animation."
        }
    }
}

/*
    Animator.Appear(e,d)

    e   element
    d   duration
    */
Animator.Appear = function(e, d) {
    d = d || 0;
    return function(t) {
        var $svg = $(t).svg('get');
        $(e, $svg.root()).each( function(){
            $(this).animate({'svgOpacity': 1.}, d);
        })
    }
}

/*
    Animator.Disappear(e,d)

    e   element
    d   duration
    */
Animator.Disappear = function(e, d) {
    d = d || 0;
    return function(t) {
        var $svg = $(t).svg('get');
        $(e, $svg.root()).each( function(){
            $(this).animate({'svgOpacity': 0.}, d);
        })
    }
}

/*
    Animator.Transform(e,tr,d)

    e   element
    tr  the transformation
    d   duration
    */
Animator.Transform = function(e,tr,d) {
    d = d || 0;
    return function(t) {
        var $svg = $(t).svg('get');
        $(e, $svg.root()).each( function(){
            $(this).animate({'svgTransform': tr}, d);
        })
    }
}


