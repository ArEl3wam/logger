from src.test_suite.test_suite import TestSuite

from src.generators.testsuite_generator import TestSuiteSampleGenerator
from src.generators.testcase_generator import TestCaseSampleGenerator
from src.generators.validationtag_generator import ValidationTagSampleGenerator
from src.generators.validationpoint_generator import ValidationPointSampleGenerator


test_suite_sample_generator = TestSuiteSampleGenerator()
test_case_sample_generator = TestCaseSampleGenerator()
validation_tag_sample_generator = ValidationTagSampleGenerator()
validation_point_sample_generator = ValidationPointSampleGenerator()

for _ in range(1):
    test_suite: TestSuite = TestSuite(test_suite_sample_generator.generate())
    for _ in range(1):
        tc = test_suite.create_test_case(test_case_sample_generator.generate())
        for _ in range(1):
            vt = tc.create_validation_tag(validation_tag_sample_generator.generate())
            for _ in range(1):
                vp = vt.create_validation_point(validation_point_sample_generator.generate())
                for _ in range(1):
                    vp.create_result(**validation_point_sample_generator.generate_result())

    for _ in range(1):
        vt = test_suite.create_validation_tag(validation_tag_sample_generator.generate())

    test_suite.push_all()
