/*!
 * jQuery twitter bootstrap wizard plugin
 * Examples and documentation at: http://github.com/VinceG/twitter-bootstrap-wizard
 * version 1.0
 * Requires jQuery v1.3.2 or later
 * Supports Bootstrap 2.2.x, 2.3.x, 3.0
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 * Authors: Vadim Vincent Gabriel (http://vadimg.com), Jason Gill (www.gilluminate.com)
 */
;(function($) {
var bootstrapWizardCreate = function(element, options) {
	var element = $(element);
	var obj = this;

	steps = mUtil.findAll(element, '.m-wizard__step');

	progress = mUtil.find(element, '.m-wizard__progress .progress-bar');
	btnSubmit = mUtil.find(element, '[data-wizard-action="submit"]');
	btnNext = mUtil.find(element, '[data-wizard-action="next"]');
	btnPrev = mUtil.find(element, '[data-wizard-action="prev"]');
	btnLast = mUtil.find(element, '[data-wizard-action="last"]');
	btnFirst = mUtil.find(element, '[data-wizard-action="first"]');

	// selector skips any 'li' elements that do not contain a child with a tab data-toggle
	var baseItemSelector = 'li:has([data-toggle="tab"])';

	// Merge options with defaults
	var $settings = $.extend({}, $.fn.bootstrapWizard.defaults, options);
	var $activeTab = null;
	var $navigation = null;
	
	this.rebindClick = function(selector, fn)
	{
		selector.unbind('click', fn).bind('click', fn);
	}

	this.fixNavigationButtons = function() {
		// Get the current active tab
		if(!$activeTab.length) {
			// Select first one
			$navigation.find('a:first').tab('show');
			$activeTab = $navigation.find(baseItemSelector + ':first');
		}

		// See if we're currently in the first/last then disable the previous and last buttons
		$($settings.previousSelector, element).toggleClass('disabled', (obj.firstIndex() >= obj.currentIndex()));
		$($settings.nextSelector, element).toggleClass('disabled', (obj.currentIndex() >= obj.navigationLength()));

		// We are unbinding and rebinding to ensure single firing and no double-click errors
		obj.rebindClick($($settings.nextSelector, element), obj.next);
		obj.rebindClick($($settings.previousSelector, element), obj.previous);
		obj.rebindClick($($settings.lastSelector, element), obj.last);
		obj.rebindClick($($settings.firstSelector, element), obj.first);

		if($settings.onTabShow && typeof $settings.onTabShow === 'function' && $settings.onTabShow($activeTab, $navigation, obj.currentIndex())===false){
			return false;
		}
	};

	this.next = function(e) {

		// If we clicked the last then dont activate this
		if(element.hasClass('last')) {
			return false;
		}

		function csrfSafeMethod(method) {
    		// these HTTP methods do not require CSRF protection
    		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		function sameOrigin(url) {
			// test that a given url is a same-origin URL
			// url could be relative or scheme relative or absolute
			var host = document.location.host; // host + port
			var protocol = document.location.protocol;
			var sr_origin = '//' + host;
			var origin = protocol + sr_origin;
			// Allow absolute or scheme relative URLs to same origin
			return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
				(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
				// or any other URL that isn't scheme relative or absolute i.e relative.
				!(/^(\/\/|http:|https:).*/.test(url));
			}
		$curIndex = obj.currentIndex();
		//send all form data, let python figure it out on the backend based on type.
		var data = new FormData(document.getElementById('form-wizard-onboarding'));
		var name = $('[name=name]').val();
		var type = $curIndex;
		var onboarding = $('[name=onboardingid]').val();
		//For some reason select stuff doesn't....come...across...which is most of the codebase...need to fix
		if (type == 0) {
			//append data manually for now
			var primaryContact = $('#pc option:selected').val();
			var pcName = $('#pc option:selected').attr('name');

			var itSupport = $('#is option:selected').val();
			var itsName = $('#is option:selected').attr('name');

			var itPlan = $('#it option:selected').val();
			var itpName = $('#it option:selected').attr('name');

			var accountsPayable = $('#ap option:selected').val();
			var apName = $('#ap option:selected').attr('name');

			var buildingAccess = $('#em option:selected').val();
			var baName = $('#em options:selected').attr('name');

			var complianceOfficer = $('#co option:selected').val();
			var coName = $('#co option:selected').attr('name');

			var vendorManagement = $('#vm option:selected').val();
			var vmName = $('#vm option:selected').attr('name');

			//nonContact
            var phoneNumber = $('#tel input').val();
            var address = $('#address input').val();

            data.append('phoneNumber',phoneNumber);
            data.append('address',address);

			data.append('primaryContact', primaryContact);
			data.append('pcName',pcName);
			data.append('itSupport', itSupport);
			data.append('itsName', itsName);
			data.append('itPlan', itPlan);
			data.append('itpName', itpName);
			data.append('accountsPayable', accountsPayable);
			data.append('apName', apName);
			data.append('buildingAccess', buildingAccess);
			data.append('baName', baName);
			data.append('complianceOfficer', complianceOfficer);
			data.append('coName', coName);
			data.append('vendorManagement', vendorManagement);
			data.append('vmName', vmName);


		}
		else if (type == 1 ){

			console.log('Processing Networking Stuff');
			var netdata = { fwlist: [], swlist: [], aplist: []};

			fwData = document.querySelectorAll("[id^='fwRow']");

			//Firewall Listing Loop, jquery
			$('div[id^="fieldFW"]').each(function(index,item) {

				fwitem = $(this).find('#fwbrand_0 option:selected').val();
				fwbrand = $(this).find('#fwbrand_0 option:selected').text();

				modelid = $(this).find('#fwmodel_0 option:selected').val();
				modeltext = $(this).find('#fwmodel_0 option:selected').text();

				replace = $(this).find('#fwreplace_0 option:selected').val();


				netdata.fwlist.push({"fwid": fwitem, "fwbrand": fwbrand, "fwmodelid":modelid,"fwmodel":modeltext,"replace":replace});
			});

			//SW Listing Loop, jquery
			$('div[id^="fieldSW"]').each(function(index,item) {

				fwitem = $(this).find('#fwbrand_0 option:selected').val();
				fwbrand = $(this).find('#fwbrand_0 option:selected').text();

				modelid = $(this).find('#fwmodel_0 option:selected').val();
				modeltext = $(this).find('#fwmodel_0 option:selected').text();

				replace = $(this).find('#fwreplace_0 option:selected').val();


				netdata.swlist.push({"swid": fwitem, "swbrand": fwbrand, "swmodelid":modelid,"swmodel":modeltext,"replace":replace});
			});

			//ap Listing Loop, jquery
			$('div[id^="fieldAP"]').each(function(index,item) {

				fwitem = $(this).find('#fwbrand_0 option:selected').val();
				fwbrand = $(this).find('#fwbrand_0 option:selected').text();

				modelid = $(this).find('#fwmodel_0 option:selected').val();
				modeltext = $(this).find('#fwmodel_0 option:selected').text();

				replace = $(this).find('#fwreplace_0 option:selected').val();


				netdata.aplist.push({"apid": fwitem, "apbrand": fwbrand, "apmodelid":modelid,"apmodel":modeltext,"replace":replace});
			});




			data.append('netdata',netdata);
			console.log(netdata);


		}
		data.append('type', type);
		data.append('onboarding', onboarding);
		$.ajax({
				 type: 'POST',
				 beforeSend: function(xhr, settings) {
						if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
							// Send the token to same-origin, relative URLs only.
							// Send the token only if the method warrants CSRF protection
							// Using the CSRFToken value acquired earlier
							xhr.setRequestHeader("X-CSRFToken",$('[name=csrfmiddlewaretoken]').val());
						}
					},
				 url: "",
				 data: data,
				 processData: false,
				 contentType: false,
				 success: function(json) {
					console.log(json);
				 }
			 });


		if($settings.onNext && typeof $settings.onNext === 'function' && $settings.onNext($activeTab, $navigation, obj.nextIndex())===false){
			return false;
		}

		console.log($curIndex);
		// Did we click the last button
		$index = obj.nextIndex();
		console.log($index);
		if($index > obj.navigationLength()) {
		} else {
			$navigation.find(baseItemSelector + ':eq('+$index+') a').tab('show');
		}
	};

	this.previous = function(e) {

		// If we clicked the first then dont activate this
		if(element.hasClass('first')) {
			return false;
		}
		console.log("Clicked Previous")
		if($settings.onPrevious && typeof $settings.onPrevious === 'function' && $settings.onPrevious($activeTab, $navigation, obj.previousIndex())===false){
			return false;
		}

		$index = obj.previousIndex();
		if($index < 0) {
		} else {
			$navigation.find(baseItemSelector + ':eq('+$index+') a').tab('show');
		}
	};

	this.first = function(e) {
		if($settings.onFirst && typeof $settings.onFirst === 'function' && $settings.onFirst($activeTab, $navigation, obj.firstIndex())===false){
			return false;
		}

		// If the element is disabled then we won't do anything
		if(element.hasClass('disabled')) {
			return false;
		}
		$navigation.find(baseItemSelector + ':eq(0) a').tab('show');

	};
	this.last = function(e) {
		if($settings.onLast && typeof $settings.onLast === 'function' && $settings.onLast($activeTab, $navigation, obj.lastIndex())===false){
			return false;
		}

		// If the element is disabled then we won't do anything
		if(element.hasClass('disabled')) {
			return false;
		}
		$navigation.find(baseItemSelector + ':eq('+obj.navigationLength()+') a').tab('show');
	};
	this.currentIndex = function() {
		return $navigation.find(baseItemSelector).index($activeTab);
	};
	this.firstIndex = function() {
		return 0;
	};
	this.lastIndex = function() {
		return obj.navigationLength();
	};
	this.getIndex = function(e) {
		return $navigation.find(baseItemSelector).index(e);
	};
	this.nextIndex = function() {
		return $navigation.find(baseItemSelector).index($activeTab) + 1;
	};
	this.previousIndex = function() {
		return $navigation.find(baseItemSelector).index($activeTab) - 1;
	};
	this.navigationLength = function() {
		return $navigation.find(baseItemSelector).length - 1;
	};
	this.activeTab = function() {
		return $activeTab;
	};
	this.nextTab = function() {
		console.log("Clikced Next")
		return $navigation.find(baseItemSelector + ':eq('+(obj.currentIndex()+1)+')').length ? $navigation.find(baseItemSelector + ':eq('+(obj.currentIndex()+1)+')') : null;
	};
	this.previousTab = function() {
		if(obj.currentIndex() <= 0) {
			return null;
		}
		return $navigation.find(baseItemSelector + ':eq('+parseInt(obj.currentIndex()-1)+')');
	};
	this.show = function(index) {
		if (isNaN(index)) {
			return element.find(baseItemSelector + ' a[href=#' + index + ']').tab('show');
		}
		else {
			return element.find(baseItemSelector + ':eq(' + index + ') a').tab('show');
		}
	};
	this.disable = function(index) {
		$navigation.find(baseItemSelector + ':eq('+index+')').addClass('disabled');
	};
	this.enable = function(index) {
		$navigation.find(baseItemSelector + ':eq('+index+')').removeClass('disabled');
	};
	this.hide = function(index) {
		$navigation.find(baseItemSelector + ':eq('+index+')').hide();
	};
	this.display = function(index) {
		$navigation.find(baseItemSelector + ':eq('+index+')').show();
	};
	this.remove = function(args) {
		var $index = args[0];
		var $removeTabPane = typeof args[1] != 'undefined' ? args[1] : false;
		var $item = $navigation.find(baseItemSelector + ':eq('+$index+')');

		// Remove the tab pane first if needed
		if($removeTabPane) {
			var $href = $item.find('a').attr('href');
			$($href).remove();
		}

		// Remove menu item
		$item.remove();
	};
	
	var innerTabClick = function (e) {
		// Get the index of the clicked tab
		var clickedIndex = $navigation.find(baseItemSelector).index($(e.currentTarget).parent(baseItemSelector));
		if($settings.onTabClick && typeof $settings.onTabClick === 'function' && $settings.onTabClick($activeTab, $navigation, obj.currentIndex(), clickedIndex)===false){
			return false;
		}
	};
	
	var innerTabShown = function (e) {  // use shown instead of show to help prevent double firing
		$element = $(e.target).parent();
		var nextTab = $navigation.find(baseItemSelector).index($element);

		// If it's disabled then do not change
		if($element.hasClass('disabled')) {
			return false;
		}

		if($settings.onTabChange && typeof $settings.onTabChange === 'function' && $settings.onTabChange($activeTab, $navigation, obj.currentIndex(), nextTab)===false){
				return false;
		}

		$activeTab = $element; // activated tab
		obj.fixNavigationButtons();
	};
	
	this.resetWizard = function() {
		
		// remove the existing handlers
		$('a[data-toggle="tab"]', $navigation).off('click', innerTabClick);
		$('a[data-toggle="tab"]', $navigation).off('shown', innerTabShown);
		
		// reset elements based on current state of the DOM
		$navigation = element.find('ul:first', element);
		$activeTab = $navigation.find(baseItemSelector + '.active', element);
		
		// re-add handlers
		$('a[data-toggle="tab"]', $navigation).on('click', innerTabClick);
		$('a[data-toggle="tab"]', $navigation).on('shown shown.bs.tab', innerTabShown);
		
		obj.fixNavigationButtons();
	};

	$navigation = element.find('#m-wizard__step--current', element);
	$activeTab = $navigation.find(baseItemSelector + '.active', element);

	if(!$navigation.hasClass($settings.tabClass)) {
		$navigation.addClass($settings.tabClass);
	}

	// Load onInit
	if($settings.onInit && typeof $settings.onInit === 'function'){
		$settings.onInit($activeTab, $navigation, 0);
	}

	// Load onShow
	if($settings.onShow && typeof $settings.onShow === 'function'){
		$settings.onShow($activeTab, $navigation, obj.nextIndex());
	}

	$('a[data-toggle="tab"]', $navigation).on('click', innerTabClick);

};
$.fn.bootstrapWizard = function(options) {
	//expose methods
	if (typeof options == 'string') {
		var args = Array.prototype.slice.call(arguments, 1)
		if(args.length === 1) {
			args.toString();
		}
		return this.data('bootstrapWizard')[options](args);
	}
	return this.each(function(index){
		var element = $(this);
		// Return early if this element already has a plugin instance
		if (element.data('bootstrapWizard')) return;
		// pass options to plugin constructor
		var wizard = new bootstrapWizardCreate(element, options);
		// Store plugin object in this element's data
		element.data('bootstrapWizard', wizard);
		// and then trigger initial change
		wizard.fixNavigationButtons();
	});
};

// expose options
$.fn.bootstrapWizard.defaults = {
	tabClass:         'm-wizard__nav',
	nextSelector:     '.wizard .btnNext',
	previousSelector: '.wizard .btnPrev',
	firstSelector:    '.wizard .btnFirst',
	lastSelector:     '.wizard .btnLast',
	onShow:           null,
	onInit:           null,
	onNext:           null,
	onPrevious:       null,
	onLast:           null,
	onFirst:          null,
	onTabChange:      null, 
	onTabClick:       null,
	onTabShow:        null

};



})(jQuery);


$(document).ready(function() {
  	$('#m_wizard').bootstrapWizard();
  	console.log('Wizard Engaged');
});