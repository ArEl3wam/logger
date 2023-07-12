from time import time
from src.generators.fake_data_generator.testsuite_generator import TestSuiteSampleGenerator
from src.generators.fake_data_generator.validationtag_generator import ValidationTagSampleGenerator
from src.test_suite.test_suite import TestSuite
from src.generators.fake_data_generator.testcase_generator import TestCaseSampleGenerator
from src.generators.fake_data_generator.validationpoint_generator import ValidationPointSampleGenerator


test_suite_sample_generator = TestSuiteSampleGenerator()
test_case_sample_generator = TestCaseSampleGenerator()
validation_tag_sample_generator = ValidationTagSampleGenerator()
validation_point_sample_generator = ValidationPointSampleGenerator()

NUMBER_OF_TEST_SUITES = 1
NUMBER_OF_TEST_CASES = 1
NUMBER_OF_VALIDATION_TAGS = 1
NUMBER_OF_VALIDATION_POINTS = 1

start_time = time()


for _ in range(NUMBER_OF_TEST_SUITES):
    test_suite: TestSuite = TestSuite(test_suite_sample_generator.generate())

    for _ in range(NUMBER_OF_TEST_CASES):
        tc = test_suite.create_test_case(test_case_sample_generator.generate())
        for _ in range(NUMBER_OF_VALIDATION_TAGS):
            vt = tc.create_validation_tag(validation_tag_sample_generator.generate())
            for _ in range(NUMBER_OF_VALIDATION_POINTS):
                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("fail"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("fail"))
                vp.create_result(**validation_point_sample_generator.generate_result("fail"))

            vt = tc.create_validation_tag(validation_tag_sample_generator.generate())
            for _ in range(NUMBER_OF_VALIDATION_POINTS):
                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

        tc = test_suite.create_test_case(test_case_sample_generator.generate())
        for _ in range(NUMBER_OF_VALIDATION_TAGS):
            vt = tc.create_validation_tag(validation_tag_sample_generator.generate())
            for _ in range(NUMBER_OF_VALIDATION_POINTS):
                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vt = tc.create_validation_tag(validation_tag_sample_generator.generate())

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))

                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
                vp.create_result(**validation_point_sample_generator.generate_result("pass"))
    test_suite.push_all()

print("Time elapsed: {time_elapsed}".format(time_elapsed=time() - start_time))
