var WizardDemo = function() {
	$("#m_wizard");
	var e, r, i = $("#m_form");
	return {
		init: function() {
			var n;
			$("#m_wizard"), i = $("#m_form"), (r = new mWizard("m_wizard", {
				startStep: 1
			})).on("beforeNext", function(r) {
				!0 !== e.form() && r.stop();
				console.log('BEFORE CHANGE');
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

				//send all form data, let python figure it out on the backend based on type.
				var data = new FormData(document.getElementById('m_form'));
				var data = new FormData();
				var name = $('[name=name]').val();
				data.append('name',name)
				var type = r.getStep()-1;
				var onboarding = $('[name=onboardingid]').val();
				console.log(type);
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
					var baName = $('#em option:selected').attr('name');

					var complianceOfficer = $('#co option:selected').val();
					var coName = $('#co option:selected').attr('name');

					var vendorManagement = $('#vm option:selected').val();
					var vmName = $('#vm option:selected').attr('name');

					//nonContact
					var phoneNumber = $('#tel').val();
					var address = $('#address').val();

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
			var netdata = { fwlist: {}, swlist: [], aplist: []};
			var localip = $('#localip input').val();
			var extip = $('#extip input').val();
			var isp = $('#isp option:selected').val();
			var speed = $('#speed option:selected').val();
			var fwlist = [];
			var swlist = [];

			data.append('localip',localip);
			data.append('extip', extip);
			data.append('isp', isp);
			data.append('speed', speed);

			fwData = document.querySelectorAll("[id^='fwRow']");
			fwList = "";
			swList = "";
			apList = "";

			//Firewall Listing Loop, jquery
			$('div[id^="fieldFW"]').each(function(index,item) {

				fwitem = $(this).find('#fwbrand_0 option:selected').val();
				fwbrand = $(this).find('#fwbrand_0 option:selected').text();

				modelid = $(this).find('#fwmodel_0 option:selected').val();
				modeltext = $(this).find('#fwmodel_0 option:selected').text();

				replace = $(this).find('#fwreplace_0 option:selected').val();


				fwList += "fwid=" +fwitem + ",";
				fwList += "fwbrand=" + fwbrand + ",";
				fwList += "fwmodelid=" + modelid + ",";
				fwList += "fwmodel=" + modeltext + ",";
				fwList += "replace=" + replace + ";";

			});

			data.append('fwList',fwList);

			//SW Listing Loop, jquery
			$('div[id^="fieldSW"]').each(function(index,item) {

				fwitem = $(this).find('#swbrand_0 option:selected').val();
				fwbrand = $(this).find('#swbrand_0 option:selected').text();

				modelid = $(this).find('#swmodel_0 option:selected').val();
				modeltext = $(this).find('#swmodel_0 option:selected').text();

				replace = $(this).find('#swreplace_0 option:selected').val();


				swList += "swid=" + fwitem + ",";
				swList += "swbrand=" + fwbrand + ",";
				swList += "modelid=" + modelid + ",";
				swList += "modeltext=" + modeltext + ",";
				swList += "replace=" + replace +";";

			});

			data.append('swList', swList);

			//ap Listing Loop, jquery
			$('div[id^="fieldAP"]').each(function(index,item) {

				fwitem = $(this).find('#apbrand_0 option:selected').val();
				fwbrand = $(this).find('#apbrand_0 option:selected').text();

				modelid = $(this).find('#apmodel_0 option:selected').val();
				modeltext = $(this).find('#apmodel_0 option:selected').text();

				replace = $(this).find('#apreplace_0 option:selected').val();


				apList += "apid=" + fwitem + ",";
				apList += "apbrand=" + fwbrand + ",";
				apList += "modelid=" + modelid + ",";
				apList += "modeltext=" + modeltext + ",";
				apList += "replace=" + replace +";";
			});

			data.append('apList', apList);


		}
		else if (type == 2 ){
					//ONWARDS


                }
				data.append('type', type);
				data.append('onboarding', onboarding);
				//console.log(data);
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





			}), r.on("change", function(e) {
				mUtil.scrollTop()


			}), r.on("change", function(e) {
				1 === e.getStep() && alert(1)
			}),
			e = i.validate({
				debug: true,
				//BUG
				//There is a bug that prevents submission the below is a workaround. I think it has to due with Step 1, but could be Step 2.
				ignore: '.m-input',
				//END BUG
				invalidHandler:function(e,r){
					mUtil.scrollTop();
					console.log('invalid');
				},
				submitHandler: function(e) {}
			}), (n = i.find('[data-wizard-action="submit"]')).on("click", function(r) {
				r.preventDefault(), e.form() && (mApp.progress(n), i.ajaxSubmit({
					success: function() {
						mApp.unprogress(n), swal({
							title: "",
							text: "The application has been successfully submitted!",
							type: "success",
							confirmButtonClass: "btn btn-secondary m-btn m-btn--wide"
						})
					}
				}))
			})
		}
	}
}();
jQuery(document).ready(function() {
	WizardDemo.init()
});
var BootstrapSelect = {
	init: function() {
		$(".m_selectpicker").selectpicker()
	}
};
jQuery(document).ready(function() {
	BootstrapSelect.init()
});