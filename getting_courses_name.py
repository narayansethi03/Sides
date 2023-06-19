# What this does?

# It gets the text data from the specified HTML class. It is done using BeautifulSoup's `find_all`. The HTML variable contains the string from where the data is to be extracted.

html = '''<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_53" value="53_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_53-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Difficult Conversations</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=53_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_62" value="62_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_62-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Active Shooter: Responding in the Worst-Case Scenario</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=62_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_63" value="63_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_63-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Workplace Violence for Employees</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=63_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_74" value="74_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_74-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Workplace Sustainability Principles: The Golden R’s</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=74_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_75" value="75_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_75-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Workplace Sustainability Principles: The 3 Pillars of Sustainability</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=75_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_99" value="99_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_99-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Customer Service - What do Customers Want</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=99_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_100" value="100_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_100-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Providing Telephone Customer Service</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=100_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_122" value="122_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_122-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Office Etiquette.. an Introduction</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=122_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_140" value="140_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_140-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Five Golden Rules</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=140_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_148" value="148_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_148-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Customer Care</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=148_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_150" value="150_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_150-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Workplace Violence Program</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=150_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_151" value="151_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_151-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Training and Development</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=151_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_181" value="181_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_181-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Advanced Call Center Training</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=181_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_182" value="182_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_182-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Handling Dangerous Workplace Situations</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=182_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_193" value="193_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_193-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Risks of Social Networking</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=193_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_200" value="200_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_200-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Basic Quality Roles and Responsibilities</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=200_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_230" value="230_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_230-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Challenges of Social Networking</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=230_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_252" value="252_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_252-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">	</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=252_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_253" value="253_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_253-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Getting Organized</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=253_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_257" value="257_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_257-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Responding to Customer Complaints</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=257_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>
<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_259" value="259_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_259-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Record Keeping</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=259_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_264" value="264_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_264-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Workplace Organization</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=264_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_340" value="340_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_340-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Cross Cultural Intelligence</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=340_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_362" value="362_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_362-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Renegotiate Deadlines - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=362_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_390" value="390_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_390-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Adopting a learning mindset</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=390_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_428" value="428_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_428-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Setting Up Your Desk For Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=428_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_438" value="438_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_438-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Appreciate every moment and enjoy your well-being at work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=438_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_469" value="469_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_469-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Adding value to your meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=469_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_471" value="471_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_471-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Managing an excessive workload with the LIMITER method</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=471_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_472" value="472_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_472-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Managing projects with the Kanban method</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=472_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_475" value="475_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_475-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Creating connections at work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=475_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_485" value="485_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_485-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Executive Skills on the Job</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=485_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_509" value="509_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_509-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What Is a VUCA Environment?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=509_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_529" value="529_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_529-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Making a Decision in a Meeting</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=529_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_530" value="530_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_530-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Speak Out Against Offensive Workplace Behavior</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=530_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_531" value="531_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_531-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Disrespect and Crossing the Line</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=531_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_560" value="560_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_560-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Build Trust and Credibility</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=560_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_565" value="565_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_565-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Equal Employment Opportunity - Blue Collar Workers</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=565_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_566" value="566_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_566-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Drugs &amp; Alcohol - Blue Collar Workers</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=566_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_569" value="569_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_569-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Health at Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=569_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_570" value="570_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_570-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Accomplishment at Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=570_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_572" value="572_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_572-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Engagement at Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=572_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_596" value="596_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_596-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Making Your Desk Make You More Productive</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=596_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_616" value="616_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_616-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Hope Theory at Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=616_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_625" value="625_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_625-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Switch On Respect</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=625_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_635" value="635_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_635-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Motivate a Co-worker</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=635_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_650" value="650_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_650-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Meeting Customer Needs</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=650_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_706" value="706_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_706-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Company Information - Handle With Care</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=706_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_707" value="707_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_707-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Company Assets and Occasional Use</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=707_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_708" value="708_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_708-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Character Matters! Standing on Principle</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=708_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_712" value="712_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_712-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Difficult Conversations (CPD Certified)</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=712_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_728" value="728_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_728-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">4 Essentials for a Respectful Workplace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=728_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_729" value="729_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_729-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">4 Strategies for Building Collaboration</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=729_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_735" value="735_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_735-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">ABLE High Achiever</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=735_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_738" value="738_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_738-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Learn to Set Boundaries</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=738_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_745" value="745_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_745-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Respect in the workplace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=745_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_748" value="748_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_748-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Effective meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=748_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_752" value="752_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_752-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Managing Fatigue in the Workplace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=752_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_753" value="753_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_753-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Code of Conduct - Office Workers</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=753_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_754" value="754_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_754-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Consultation - Office Workers</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=754_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_755" value="755_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_755-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Behaviour</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=755_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_758" value="758_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_758-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Social and Cultural Awareness</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=758_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_759" value="759_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_759-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">More Formal Meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=759_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_765" value="765_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_765-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The Importance Of Top Quality Telephone Skills</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=765_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_767" value="767_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_767-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Handling Customer Concerns &amp; Complaints - Responding On The Phone</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=767_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_774" value="774_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_774-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Employee Engagement</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=774_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_775" value="775_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_775-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">10 Minute Working with Other Departments</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=775_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_796" value="796_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_796-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Keeping an open mind</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=796_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_805" value="805_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_805-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">General small talk at work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=805_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_820" value="820_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_820-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Coworkers: The Procrastinator</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=820_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_832" value="832_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_832-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Accountability: What is Accountability?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=832_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_840" value="840_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_840-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Meeting Behavior Expectations</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=840_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_843" value="843_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_843-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Delegating with Clear Expectations</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=843_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_849" value="849_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_849-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Surviving an Unreliable Colleague</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=849_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_853" value="853_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_853-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Gender Identity in the Workplace (CPD Certified)</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=853_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_854" value="854_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_854-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Maintaining Changes to Workplace Culture (CPD Certified)</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=854_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_859" value="859_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_859-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Stay Focused in Meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=859_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_861" value="861_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_861-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Building Relationships with Colleagues</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=861_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_864" value="864_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_864-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Information for Success</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=864_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_868" value="868_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_868-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Capture and Share Best Practices</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=868_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_881" value="881_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_881-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Being Consistent with Company Values</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=881_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_882" value="882_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_882-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Working with Others Within the Company</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=882_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_885" value="885_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_885-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Be Interested</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=885_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_886" value="886_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_886-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Structuring a Judgment to Reduce Errors</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=886_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_887" value="887_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_887-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Break the Crazy Busy Cycle</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=887_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_889" value="889_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_889-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Relaxing while working</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=889_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_892" value="892_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_892-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Mindfulness at Work: what does that involve?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=892_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_893" value="893_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_893-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Creating a healthier working environment</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=893_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_898" value="898_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_898-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Drawing Inspiration from Success Stories: The Imitation Trap</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=898_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_907" value="907_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_907-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">10 Minute Creativity and Innovation</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=907_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_921" value="921_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_921-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Workplace Violence in Industrial Environments - Dealing with Violent Behavior</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=921_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_936" value="936_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_936-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Productive Meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=936_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_948" value="948_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_948-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Be a Significant Meeting Member</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=948_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_949" value="949_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_949-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Essential Project Plan Components</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=949_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_955" value="955_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_955-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Increase the Level of Challenge at Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=955_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_962" value="962_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_962-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Prepare for Any Meeting</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=962_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_964" value="964_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_964-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Company Jobs and Opportunities</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=964_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_965" value="965_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_965-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Organizing Your Workspace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=965_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_966" value="966_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_966-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Learn about the Company and Customers</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=966_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_969" value="969_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_969-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Increase Your Personal Engagement</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=969_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_970" value="970_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_970-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Support the Organization’s Vision and Strategy</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=970_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_971" value="971_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_971-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Strengthen Job Required Skills</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=971_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_972" value="972_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_972-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Supporting Company Values</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=972_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_980" value="980_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_980-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Resources for Success</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=980_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1004" value="1004_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1004-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Connecting with Others</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1004_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1005" value="1005_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1005-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Be Assertive with your Boss</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1005_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1010" value="1010_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1010-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Close A Difficult Conversation - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1010_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1017" value="1017_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1017-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">S.O.S. - Your Message Emergency</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1017_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1026" value="1026_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1026-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Curing work overload</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1026_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1034" value="1034_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1034-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Short Fixes for Executive Skill Weaknesses</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1034_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1044" value="1044_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1044-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Making an Impact</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1044_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1048" value="1048_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1048-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What Excites You at Work?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1048_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1054" value="1054_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1054-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The Right Level of Challenge</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1054_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1055" value="1055_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1055-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Managing urgent client requests</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1055_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1084" value="1084_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1084-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Objection Handling Masterclass</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1084_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1085" value="1085_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1085-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Overcome The Fear of Rejection</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1085_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1106" value="1106_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1106-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Pre-Meeting Mindset &amp; Objective Setting</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1106_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1109" value="1109_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1109-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The Power of Values</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1109_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1111" value="1111_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1111-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Successful Follow Up Calls</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1111_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1114" value="1114_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1114-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Answer A Call In The Right Way - First Impressions Count</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1114_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1125" value="1125_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1125-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Formula for Success 11.2.2</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1125_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1127" value="1127_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1127-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How Often Do You Take These Situations Personally?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1127_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1128" value="1128_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1128-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Overcome Objections</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1128_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1132" value="1132_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1132-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How to use 5S in your office</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1132_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1133" value="1133_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1133-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What It Means to Be Customer Orientated</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1133_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1143" value="1143_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1143-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Prospecting - Why You Should Lose "Touching Base"</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1143_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1160" value="1160_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1160-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Professionalism in the Workplace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1160_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1170" value="1170_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1170-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Pre-Meeting Mindset &amp; Objective Setting</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1170_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1174" value="1174_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1174-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Building rapport</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1174_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1178" value="1178_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1178-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Customers Face To Face - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1178_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1180" value="1180_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1180-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Handle A Complaint - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1180_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1181" value="1181_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1181-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What Do Our Customers Expect From Us? - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1181_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1193" value="1193_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1193-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Sorry</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1193_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1195" value="1195_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1195-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Privilege</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1195_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1197" value="1197_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1197-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing with complaints: Customer Service</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1197_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1218" value="1218_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1218-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Respect at work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1218_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1225" value="1225_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1225-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Treating customers fairly</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1225_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1230" value="1230_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1230-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Working from home checklist</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1230_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1233" value="1233_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1233-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Working collaboratively online</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1233_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1235" value="1235_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1235-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Social media in the workplace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1235_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1237" value="1237_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1237-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Continuing the kindness</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1237_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1285" value="1285_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1285-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Know Your Stuff</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1285_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1290" value="1290_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1290-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Building Resilience At Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1290_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1291" value="1291_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1291-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Mental Health At Work - Overview</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1291_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1299" value="1299_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1299-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Speed Wins</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1299_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1301" value="1301_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1301-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Time Stealers - How Do We Identify Them?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1301_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1304" value="1304_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1304-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Be Assertive With Your Boss</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1304_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1305" value="1305_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1305-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">5 Prospecting Mistakes to Avoid</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1305_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1307" value="1307_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1307-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Are You Having An Active Working Day?</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1307_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1314" value="1314_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1314-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Successful Follow Up Calls</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1314_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1323" value="1323_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1323-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Alcohol &amp; Drugs at work (Microvideo only)</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1323_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1324" value="1324_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1324-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Difficult Conversations</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1324_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1325" value="1325_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1325-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Your Development - Organisational Objectives</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1325_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1331" value="1331_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1331-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Safeguarding dos and don'ts</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1331_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1353" value="1353_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1353-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What is Employee Engagement: Employee Engagement</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1353_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1362" value="1362_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1362-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Facilitate effective meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1362_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1377" value="1377_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1377-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Handling angry customers</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1377_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1406" value="1406_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1406-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Prioritising Tasks</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1406_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1425" value="1425_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1425-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Boost Your Empathy - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1425_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1428" value="1428_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1428-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The Importance Of Follow Up - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1428_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1431" value="1431_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1431-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Stage 3 - Proposing Solutions - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1431_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1432" value="1432_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1432-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Stage 4 - Bargaining For Outcomes - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1432_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1433" value="1433_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1433-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Stage 2 - Managing The Discussion - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1433_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1434" value="1434_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1434-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Stage 1 - Planning &amp; Preparation - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1434_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1435" value="1435_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1435-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Stage 5 - Summarising &amp; Reaching An Agreement - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1435_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1456" value="1456_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1456-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Getting Organised</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1456_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1457" value="1457_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1457-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Taking Messages Over The Phone</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1457_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1470" value="1470_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1470-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Charity and volunteering</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1470_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1476" value="1476_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1476-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Politeness in Customer Service: Customer Service</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1476_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1507" value="1507_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1507-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Asking Good Questions</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1507_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1508" value="1508_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1508-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Benefits of Delegation</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1508_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1523" value="1523_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1523-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Other People’s Views (OPV)</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1523_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1525" value="1525_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1525-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Lateral Thinking for Creativity</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1525_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1527" value="1527_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1527-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Great Coaching Questions To Use At Work</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1527_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1528" value="1528_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1528-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Be Assertive With Your Boss</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1528_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1530" value="1530_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1530-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Deal With Disruptive People In Meetings</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1530_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1531" value="1531_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1531-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Manage Resources</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1531_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1533" value="1533_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1533-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The Importance Of Follow Up</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1533_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1543" value="1543_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1543-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The 6 Sources Of Workplace Pressure - Part 1</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1543_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1544" value="1544_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1544-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The 6 Sources Of Workplace Pressure - Part 2</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1544_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1558" value="1558_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1558-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Customers Over The Telephone</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1558_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1559" value="1559_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1559-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Put Callers On Hold &amp; Transferring Calls</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1559_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1562" value="1562_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1562-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">How To Avoid Objections In The First Place - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1562_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1564" value="1564_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1564-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What Does Great Customer Service Look &amp; Sound Like? - Rapid Recall</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1564_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1585" value="1585_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1585-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Coworkers: The Complainer</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1585_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1586" value="1586_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1586-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Coworkers: The Nitpicker</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1586_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1587" value="1587_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1587-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Coworkers: The Nonresponder</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1587_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1588" value="1588_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1588-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Dealing With Difficult Coworkers: The Gossip</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1588_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1600" value="1600_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1600-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Getting Flex-Agile</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1600_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1604" value="1604_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1604-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">10 Minute Returning to the Workplace</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1604_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1605" value="1605_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1605-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Building &amp; Rebuilding Trust (CPD Certified)</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1605_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1606" value="1606_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1606-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">FAIR Culture</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1606_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1608" value="1608_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1608-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">CARE in a Meaningful Way</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1608_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1621" value="1621_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1621-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Liven Up Your Culture</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1621_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1622" value="1622_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1622-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Optimize Your Meeting Productivity</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1622_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1624" value="1624_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1624-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">What is OKR? Objectives &amp; Key Results</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1624_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1626" value="1626_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1626-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">The Benefits of Collaboration</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1626_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_1628" value="1628_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_1628-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Improve Meeting Efficiency</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=1628_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_2171" value="2171_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_2171-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Character Matters at Work! The Character Makeover</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=2171_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_2196" value="2196_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_2196-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Company Information - Handle With Care</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=2196_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>

<div class="items clearfix">
<div class="item  even">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_2208" value="2208_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_2208-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Understanding Empathy</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=2208_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div><div class="item  odd">
	<div class="checkbox-column">
		<input id="assign-course-catalog-management-list-checkboxes_2452" value="2452_course" type="checkbox" name="assign-course-catalog-management-list-checkboxes[]" style="position: absolute; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px);"><span id="assign-course-catalog-management-list-checkboxes_2452-styler" class="jq-checkbox" style="display: inline-block"><span></span></span>	</div>

	<div class="poweruser-courses-name" style="margin-left: 20px;">Slips, Trips, and Falls Overview</div>
	<div class="course-type">
			E-Learning<i class="elearning"></i>		</div>
	<div class="delete-button">
			<a class="ajaxModal delete-node" data-id="" data-toggle="modal" data-modal-class="delete-node" data-modal-title="Unassign" data-buttons="[{&quot;type&quot;:&quot;submit&quot;,&quot;title&quot;:&quot;Confirm&quot;},{&quot;type&quot;:&quot;cancel&quot;,&quot;title&quot;:&quot;Cancel&quot;}]" data-url="CoursecatalogApp/CourseCatalogManagement/deleteAssignedCourse&amp;id=2452_course&amp;type_of_entry=course" modal-request-type="GET" modal-request-data="[]" data-before-loading-content="" data-after-loading-content="hideConfirmButton();" data-before-submit="" data-after-submit="updateCourseCatalogAssignCoursesContent">Unassign</a>	</div>
</div></div>
'''

from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('div', attrs={'class': 'poweruser-courses-name'})
l1=[]

for tag in tags:
    #l1.append(tag.text.strip())
    print(tag.text.strip())

pd.DataFrame(l1).to_excel('output.xlsx', header=False, index=False)
