from time import time
from src.test_suite.test_suite import TestSuite

from src.generators.testsuite_generator import TestSuiteSampleGenerator
from src.generators.testcase_generator import TestCaseSampleGenerator
from src.generators.validationtag_generator import ValidationTagSampleGenerator
from src.generators.validationpoint_generator import ValidationPointSampleGenerator


test_suite_sample_generator = TestSuiteSampleGenerator()
test_case_sample_generator = TestCaseSampleGenerator()
validation_tag_sample_generator = ValidationTagSampleGenerator()
validation_point_sample_generator = ValidationPointSampleGenerator()

NUMBER_OF_TEST_SUITES = 1
NUMBER_OF_TEST_CASES = 5
NUMBER_OF_VALIDATION_TAGS = 5
NUMBER_OF_VALIDATION_POINTS = 5

start_time = time()

for _ in range(NUMBER_OF_TEST_SUITES):
    test_suite: TestSuite = TestSuite(test_suite_sample_generator.generate())
    for _ in range(NUMBER_OF_TEST_CASES):
        tc = test_suite.create_test_case(test_case_sample_generator.generate())
        for _ in range(NUMBER_OF_VALIDATION_TAGS):
            vt = tc.create_validation_tag(validation_tag_sample_generator.generate())
            for _ in range(NUMBER_OF_VALIDATION_POINTS):
                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                for _ in range(2):
                    vp.create_result(**validation_point_sample_generator.generate_result())

    for _ in range(NUMBER_OF_VALIDATION_TAGS):
        vt = test_suite.create_validation_tag(validation_tag_sample_generator.generate())

    test_suite.push_all()

print("Time elapsed: {time_elapsed}".format(time_elapsed=time() - start_time))
