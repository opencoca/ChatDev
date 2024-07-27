- {'phase': 'DemandAnalysis', 'phaseType': 'SimplePhase', 'max_turn_step': -1, 'need_reflect': 'True'}
- {'phase': 'LanguageChoose', 'phaseType': 'SimplePhase', 'max_turn_step': -1, 'need_reflect': 'True'}
- {'phase': 'Coding', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}
- {'phase': 'CodeCompleteAll', 'phaseType': 'ComposedPhase', 'cycleNum': 10, 'Composition': [{'phase': 'CodeComplete', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}]}
- {'phase': 'CodeReview', 'phaseType': 'ComposedPhase', 'cycleNum': 3, 'Composition': [{'phase': 'CodeReviewComment', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}, {'phase': 'CodeReviewModification', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}]}
- {'phase': 'Test', 'phaseType': 'ComposedPhase', 'cycleNum': 3, 'Composition': [{'phase': 'TestErrorSummary', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}, {'phase': 'TestModification', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}]}
- {'phase': 'EnvironmentDoc', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'True'}
- {'phase': 'Manual', 'phaseType': 'SimplePhase', 'max_turn_step': 1, 'need_reflect': 'False'}