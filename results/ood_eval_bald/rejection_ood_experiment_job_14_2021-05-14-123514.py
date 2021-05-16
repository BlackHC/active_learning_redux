store = {}
store['timestamp']=1620992114
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=14']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=20
store['config']={'seed': 1255, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 100, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.490886926651001})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.8523449897766113})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8437702655792236})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.2704498767852783})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6499, 'crossentropy': 2.3039515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2347991466522217})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2812137603759766})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2149622440338135})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [44638, 46080, 44394, 9306, 13628, 52962, 41232, 21370, 58264, 11957], 'labels': [8, 8, 6, 9, -1, 5, 7, 3, -1, 0], 'scores': [0.6824395656585693, 0.8563418388366699, 0.5734820365905762, 0.9631116390228271, 0.5734160542488098, 0.7572536468505859, 0.6133536696434021, 0.8043705224990845, 0.6003392934799194, 0.8057947754859924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.9599084854125977})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.981440782546997})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.3455147743225098})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.2163748741149902})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.734, 'crossentropy': 1.7165513671875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.1241710186004639})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9848781228065491})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9642173051834106})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [44804, 34169, 39208, 12275, 10211, 20897, 23245, 9627, 54053, 9607], 'labels': [5, 1, -1, 8, 5, -1, -1, 2, 5, -1], 'scores': [0.6759114265441895, 0.5992245674133301, 0.5554819107055664, 0.6432063579559326, 0.8612738251686096, 0.7855716347694397, 0.48956042528152466, 0.5016059279441833, 0.7055019736289978, 0.5861785411834717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.669907569885254})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.8944885730743408})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.882054090499878})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.467376470565796})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7505, 'crossentropy': 1.4202474609375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.9650256037712097})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.880124568939209})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9062928557395935})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [3694, 46257, 32539, 10477, 50223, 43711, 10210, 52893, 15937, 12059], 'labels': [4, -1, 3, 2, 5, 3, 3, 4, 3, 9], 'scores': [0.5988875031471252, 0.37597739696502686, 0.5240755677223206, 0.6063486933708191, 0.45957881212234497, 0.6448993682861328, 0.5615074038505554, 0.6112551689147949, 0.5557621121406555, 0.713451087474823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.4079980850219727})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.4843425750732422})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.5137193202972412})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.4826008081436157})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8016, 'crossentropy': 1.11511533203125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.8927570581436157})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8116351962089539})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.8032550811767578})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [5191, 23154, 41613, 6097, 52975, 47513, 51127, 29061, 23629, 30127], 'labels': [2, 0, 9, 0, 2, 0, 0, 3, 5, 0], 'scores': [0.699211061000824, 0.7377971410751343, 0.6920410394668579, 0.8211491107940674, 0.7237160205841064, 0.7016870975494385, 0.7647542357444763, 0.4946868419647217, 0.6962296962738037, 0.5743714570999146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.327305793762207})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.4065430164337158})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6538176536560059})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.4988759756088257})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7536, 'crossentropy': 1.18899375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0072863101959229})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9072514772415161})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9408578276634216})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [15785, 16114, 41385, 55752, 45175, 8463, 25309, 20072, 55182, 46219], 'labels': [3, 8, -1, -1, -1, -1, 2, 3, 8, 2], 'scores': [0.4457451105117798, 0.357235848903656, 0.34185004234313965, 0.40534305572509766, 0.35076308250427246, 0.30012214183807373, 0.46167051792144775, 0.48987096548080444, 0.5089702606201172, 0.4703073501586914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.2166523933410645})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2014257907867432})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.210080623626709})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.389597773551941})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3316986560821533})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.843, 'crossentropy': 1.04980615234375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7829095125198364})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.7967783212661743})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.6937745809555054})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.7252085208892822})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [16600, 37574, 22091, 866, 56821, 53666, 38766, 21786, 21883, 23376], 'labels': [4, 5, 6, 2, -1, 7, -1, 9, -1, -1], 'scores': [0.595531702041626, 0.6432775855064392, 0.815686821937561, 0.569303423166275, 0.4077790379524231, 0.6313268542289734, 0.5062046647071838, 0.7635830640792847, 0.5080808401107788, 0.5535953044891357]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.021982192993164})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1614577770233154})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.31833815574646})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2908799648284912})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8301, 'crossentropy': 0.9115642578125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8679085969924927})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 0.8069314360618591})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.7904900312423706})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [35196, 32678, 30074, 29904, 31023, 24751, 25782, 5152, 4520, 14734], 'labels': [7, 2, 6, 2, 8, 2, 7, 3, 6, -1], 'scores': [0.36504828929901123, 0.3638480305671692, 0.4746295213699341, 0.5176950097084045, 0.33710938692092896, 0.4115602970123291, 0.49241214990615845, 0.49544066190719604, 0.4003722667694092, 0.17443525791168213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8805353045463562})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8607603311538696})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0234644412994385})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9324380159378052})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9587991237640381})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8722, 'crossentropy': 0.780776171875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7373852729797363})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6328982710838318})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.5930939316749573})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5976481437683105})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [50357, 6238, 12950, 18193, 11643, 53035, 45199, 21422, 4503, 35044], 'labels': [-1, 9, 2, -1, 5, -1, 8, 9, 9, 8], 'scores': [0.2807161808013916, 0.41469335556030273, 0.6332757472991943, 0.4187382459640503, 0.3818456530570984, 0.251595139503479, 0.6245629787445068, 0.49575936794281006, 0.6569147109985352, 0.5983132123947144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8581427335739136})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7620688676834106})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8572161197662354})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8007462620735168})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9821363091468811})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8857, 'crossentropy': 0.733771923828125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6919059753417969})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5963003039360046})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5500451326370239})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5297960638999939})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [52582, 51348, 776, 52697, 54035, 48696, 24716, 30844, 7270, 7768], 'labels': [2, 0, 0, 3, 7, 2, 5, 8, 5, 8], 'scores': [0.4813123345375061, 0.5429741442203522, 0.5268060564994812, 0.5114799737930298, 0.518540620803833, 0.5780647397041321, 0.5374910235404968, 0.40577661991119385, 0.40755563974380493, 0.5001624226570129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.791767418384552})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.684381365776062})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7671732902526855})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7381551265716553})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7826312780380249})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8861, 'crossentropy': 0.67310859375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6948535442352295})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5843415856361389})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5536031723022461})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5237575769424438})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [382, 46711, 7860, 20339, 5580, 34516, 21007, 6591, 8765, 28951], 'labels': [-1, -1, 1, 8, 4, -1, 3, -1, 3, 5], 'scores': [0.3836773633956909, 0.21068072319030762, 0.3430594205856323, 0.4226230978965759, 0.3890365958213806, 0.446661114692688, 0.42601966857910156, 0.4487473964691162, 0.5120190978050232, 0.34078481793403625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.9122366905212402})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.687069833278656})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8107162714004517})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7425011992454529})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7761261463165283})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.66546142578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7269513607025146})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5552965402603149})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5168380737304688})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5329520106315613})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [7962, 53938, 5973, 52858, 26511, 34836, 24934, 44267, 54001, 2871], 'labels': [5, 3, 6, 6, 6, 5, -1, 8, 3, 3], 'scores': [0.49707990884780884, 0.5089889764785767, 0.554520845413208, 0.571950376033783, 0.5449643135070801, 0.4523104429244995, 0.4800689220428467, 0.5624534487724304, 0.3820587396621704, 0.49318230152130127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9034099578857422})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6644502282142639})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6364482641220093})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6814274787902832})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7143035531044006})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6726821660995483})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.6234359375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7205820083618164})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5559515953063965})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.48107653856277466})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4599156379699707})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.44611304998397827})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [31777, 51314, 51331, 18018, 16202, 51043, 40726, 34946, 11696, 41229], 'labels': [4, 0, -1, 5, -1, -1, 8, 8, 5, 3], 'scores': [0.4168933629989624, 0.7359538078308105, 0.3413867950439453, 0.41049402952194214, 0.46239399909973145, 0.31174755096435547, 0.643028199672699, 0.6730329394340515, 0.5610032677650452, 0.5619099140167236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8238214254379272})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6088441610336304})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6800286769866943})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6822365522384644})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7015823125839233})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.584498095703125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7473101615905762})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5721681118011475})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5318580269813538})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5007762908935547})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [29662, 49039, 43126, 42287, 50505, 46623, 39427, 33071, 58456, 18193], 'labels': [2, -1, 3, 5, 8, 4, 5, 5, 5, -1], 'scores': [0.4257643222808838, 0.510857343673706, 0.6284929513931274, 0.6264632940292358, 0.4760814905166626, 0.4202841520309448, 0.6179938912391663, 0.5519344806671143, 0.5957497358322144, 0.5653089284896851]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8207430839538574})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6390495300292969})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6670241355895996})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6768199801445007})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7640310525894165})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9023, 'crossentropy': 0.623328759765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7222687005996704})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5897494554519653})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5253745913505554})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5158085823059082})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [30418, 22883, 37039, 3222, 33593, 37305, 57597, 56128, 49499, 6474], 'labels': [8, -1, 8, -1, 2, 1, 2, 5, 1, 6], 'scores': [0.5293673276901245, 0.4253408908843994, 0.39093634486198425, 0.24464988708496094, 0.7417151927947998, 0.6317765712738037, 0.3534891605377197, 0.5089240074157715, 0.6102951765060425, 0.6949896812438965]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8817096948623657})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6073938608169556})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6544293165206909})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6516126394271851})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6743884086608887})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.569640966796875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7442295551300049})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.585079550743103})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.522060215473175})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5476399064064026})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [9633, 37136, 15414, 16379, 44586, 10565, 2141, 6684, 52923, 54977], 'labels': [9, 9, 9, 7, 9, 1, 9, 0, 9, 3], 'scores': [0.48311883211135864, 0.40757864713668823, 0.5487768650054932, 0.588090181350708, 0.5313221216201782, 0.26106661558151245, 0.36751413345336914, 0.41508132219314575, 0.287506103515625, 0.40417802333831787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7587610483169556})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5999353528022766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5651369094848633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.548141360282898})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6611275672912598})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6319040060043335})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7469285130500793})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.493055078125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6928293704986572})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5029810070991516})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.44415539503097534})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.40851327776908875})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41668301820755005})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3985280692577362})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [26358, 39647, 56844, 11706, 274, 12373, 12934, 11534, 24587, 4050], 'labels': [3, 8, -1, 5, 6, 7, 8, 7, 8, -1], 'scores': [0.5221925973892212, 0.41488736867904663, 0.25750768184661865, 0.41302525997161865, 0.40065813064575195, 0.34424883127212524, 0.5070800185203552, 0.5872659683227539, 0.5508092641830444, 0.4071366786956787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8000355958938599})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5498220324516296})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5654820203781128})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6363825798034668})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6372454166412354})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.4946857421875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7764235734939575})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5374665260314941})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5013872385025024})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.49901384115219116})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [11202, 6932, 33663, 40354, 59177, 9876, 52889, 16525, 26779, 41568], 'labels': [9, -1, -1, -1, -1, 9, -1, -1, -1, -1], 'scores': [0.3594161868095398, 0.3692234754562378, 0.40528184175491333, 0.37187790870666504, 0.35101425647735596, 0.38229018449783325, 0.47646915912628174, 0.30567020177841187, 0.33092832565307617, 0.3773738741874695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9430257081985474})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6158828139305115})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5902496576309204})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6515005826950073})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5798455476760864})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6198359727859497})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.69269198179245})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5984762907028198})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.518963232421875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7049431800842285})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5196863412857056})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4926028549671173})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.3963930606842041})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.3902164697647095})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.3731071352958679})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.3972136676311493})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [7402, 16272, 2872, 53949, 50913, 20852, 50808, 33996, 35603, 28856], 'labels': [1, -1, -1, 6, -1, 1, -1, -1, -1, -1], 'scores': [0.4778468608856201, 0.44017839431762695, 0.5067552328109741, 0.27224022150039673, 0.3216080665588379, 0.38088279962539673, 0.34011518955230713, 0.45116734504699707, 0.23829591274261475, 0.43220090866088867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8629148006439209})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5789036750793457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5402117371559143})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5630590915679932})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6301882266998291})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5321656465530396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6986450552940369})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.631842851638794})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6003450155258179})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.459069189453125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6564871072769165})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4726179242134094})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4207152724266052})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.36481815576553345})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.3734581470489502})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3644716739654541})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.34164464473724365})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.34668004512786865})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [11083, 56838, 35326, 30718, 10722, 32782, 58337, 11976, 24066, 8859], 'labels': [-1, 5, 5, -1, 9, 6, -1, -1, -1, 8], 'scores': [0.3250408172607422, 0.674879252910614, 0.6219083070755005, 0.39920246601104736, 0.591159999370575, 0.5816703140735626, 0.4112393856048584, 0.5737634897232056, 0.32078301906585693, 0.42381995916366577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.837608277797699})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5182286500930786})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5193531513214111})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5146560668945312})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5433277487754822})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6743087768554688})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5946403741836548})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9306, 'crossentropy': 0.464164013671875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7243391275405884})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5035322904586792})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4027748703956604})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4028239846229553})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3975445628166199})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3628845810890198})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [42209, 12404, 53884, 16638, 43745, 5679, 49495, 44754, 47936, 47089], 'labels': [9, 2, 2, -1, 8, 3, 9, -1, 8, -1], 'scores': [0.44184350967407227, 0.5114259719848633, 0.5267960429191589, 0.4443260431289673, 0.49737608432769775, 0.545406848192215, 0.43558311462402344, 0.39757978916168213, 0.32350873947143555, 0.3240617513656616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8869861960411072})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6058222651481628})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48087719082832336})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5075973272323608})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5303055644035339})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5300312042236328})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.936, 'crossentropy': 0.432438916015625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8191424012184143})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4814237356185913})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4574645757675171})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4487988352775574})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39761513471603394})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [52945, 51580, 25464, 4026, 7149, 52173, 57229, 47155, 21783, 41960], 'labels': [-1, -1, 8, -1, -1, 7, -1, -1, -1, 3], 'scores': [0.41465699672698975, 0.3674807548522949, 0.43072086572647095, 0.39843249320983887, 0.3405885696411133, 0.4237595200538635, 0.4794783592224121, 0.3525291681289673, 0.3174527883529663, 0.5987870097160339]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.885339617729187})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5841173529624939})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.46890491247177124})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.553797721862793})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47465962171554565})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5957006216049194})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.43464677734375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6724644899368286})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44753527641296387})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4548514187335968})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.45107680559158325})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3953978419303894})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [47597, 6180, 12505, 46368, 37048, 20747, 52099, 36716, 25018, 17540], 'labels': [8, -1, 4, 8, 9, -1, 2, 3, 8, 1], 'scores': [0.527855634689331, 0.4052988886833191, 0.37762320041656494, 0.4225188195705414, 0.4771100878715515, 0.31464600563049316, 0.5332580208778381, 0.41780856251716614, 0.37011146545410156, 0.569378137588501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.901786744594574})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.508954644203186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5486007928848267})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4888454079627991})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5597233176231384})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5617624521255493})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5600184202194214})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.441463623046875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7133464813232422})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4809700846672058})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4194115102291107})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4218483567237854})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.375140905380249})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37845444679260254})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [15130, 41365, 34303, 19888, 15475, 10800, 5600, 11091, 10925, 13313], 'labels': [-1, 7, -1, 5, -1, 8, 6, -1, 6, -1], 'scores': [0.33501970767974854, 0.2963627576828003, 0.4297720193862915, 0.5059614777565002, 0.3887738585472107, 0.34124666452407837, 0.6837252974510193, 0.45735013484954834, 0.40853625535964966, 0.3697298765182495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9690746068954468})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5518199801445007})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5456911325454712})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5560464859008789})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5049633383750916})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49223434925079346})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5368924140930176})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5269591808319092})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5207541584968567})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9389, 'crossentropy': 0.447257861328125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7606509923934937})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4307864308357239})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3791607618331909})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.36284875869750977})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3754545748233795})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33363550901412964})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3655017018318176})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3456703722476959})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [4315, 24838, 10014, 56014, 25721, 22547, 4379, 481, 52788, 54167], 'labels': [9, -1, 7, 5, -1, -1, -1, 4, -1, -1], 'scores': [0.32961565256118774, 0.5295426249504089, 0.4035877585411072, 0.4414408206939697, 0.49005407094955444, 0.5380328893661499, 0.5110948085784912, 0.558228611946106, 0.41108238697052, 0.49483156204223633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.877260684967041})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5386713743209839})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4967813789844513})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47589296102523804})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5051083564758301})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4595820903778076})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5112683773040771})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5153383016586304})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5087213516235352})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.3842654052734375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6798897981643677})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4564782381057739})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4060482978820801})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38002943992614746})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.34598249197006226})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3517071604728699})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.33347076177597046})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.33282482624053955})
store['active_learning_steps'][24]['eval_training']['best_epoch']=8
store['active_learning_steps'][24]['acquisition']={'indices': [23968, 14540, 23434, 40953, 16964, 2580, 20869, 13352, 24136, 31690], 'labels': [7, 7, 5, -1, 8, 3, 3, 3, 1, 7], 'scores': [0.5102378129959106, 0.5941682457923889, 0.48943382501602173, 0.3396318554878235, 0.6472290754318237, 0.42797988653182983, 0.46222418546676636, 0.38130390644073486, 0.44325435161590576, 0.658277153968811]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.862555742263794})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4834722876548767})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.44738495349884033})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.49483445286750793})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4755290746688843})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5303117036819458})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.3950096435546875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7281620502471924})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5074361562728882})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41087403893470764})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.406302809715271})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3969043493270874})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [42428, 7452, 26102, 45765, 15352, 21556, 32751, 27731, 36801, 36471], 'labels': [5, 6, -1, -1, 4, -1, -1, -1, 1, 3], 'scores': [0.5017443895339966, 0.4477769136428833, 0.339799165725708, 0.303452730178833, 0.3670164942741394, 0.3932575583457947, 0.4566524028778076, 0.21141338348388672, 0.349475622177124, 0.3543536067008972]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8847489356994629})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47880345582962036})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43611592054367065})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44168153405189514})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44804856181144714})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5303713083267212})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.393419384765625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7530937194824219})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49241214990615845})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4200090169906616})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.39714720845222473})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.39277979731559753})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [54770, 30876, 5896, 36271, 27235, 7207, 23027, 46369, 37184, 11154], 'labels': [-1, -1, 8, -1, 7, 2, -1, 5, -1, 5], 'scores': [0.33019334077835083, 0.48482704162597656, 0.45172804594039917, 0.48006749153137207, 0.33247047662734985, 0.5276871919631958, 0.44719111919403076, 0.4365728497505188, 0.5477534532546997, 0.5683417916297913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8596411943435669})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4676465392112732})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5164253115653992})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45217639207839966})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5113483667373657})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4818209409713745})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4800066351890564})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9461, 'crossentropy': 0.37170244140625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7191542387008667})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5099879503250122})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.40879586338996887})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3994716703891754})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3989396095275879})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38348352909088135})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [13517, 2143, 22420, 39877, 15510, 38227, 57672, 31345, 49563, 31535], 'labels': [-1, -1, -1, 7, 2, 4, 7, 3, 8, -1], 'scores': [0.3079575300216675, 0.3153441548347473, 0.41342389583587646, 0.5127036571502686, 0.4751063585281372, 0.5331458449363708, 0.47264325618743896, 0.6002905964851379, 0.5750967860221863, 0.44312143325805664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9362220764160156})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4929673373699188})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4405282139778137})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.445753276348114})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41293472051620483})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4596717059612274})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4490400552749634})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4738762378692627})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.361138330078125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7485240697860718})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47605469822883606})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3685784339904785})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3529074490070343})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3564044237136841})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3342231512069702})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3335731625556946})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [14062, 28810, 36840, 55073, 41318, 16393, 37993, 14886, 30900, 45069], 'labels': [8, 6, -1, 4, 0, -1, -1, 9, 5, -1], 'scores': [0.6628732085227966, 0.5123670101165771, 0.48043692111968994, 0.6002599596977234, 0.28197214007377625, 0.4780256748199463, 0.4628337025642395, 0.4623183608055115, 0.30389195680618286, 0.5444055795669556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0604753494262695})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.548446774482727})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47613614797592163})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5031849145889282})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4954823851585388})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5063493251800537})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9347, 'crossentropy': 0.42892392578125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7022594213485718})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5256175994873047})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4290105402469635})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4058939218521118})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4429406523704529})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [13428, 51432, 31456, 51175, 45765, 13969, 34252, 2502, 40224, 40702], 'labels': [9, 1, 9, 4, -1, 3, 2, 7, 4, 4], 'scores': [0.6097736358642578, 0.5564112067222595, 0.6628709435462952, 0.6075214147567749, 0.29454898834228516, 0.5649586915969849, 0.5048183798789978, 0.40877270698547363, 0.5373421907424927, 0.481391966342926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0649493932724})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5600744485855103})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4646093547344208})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.504084050655365})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49541670083999634})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4496570825576782})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5211808681488037})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.493846595287323})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.523770272731781})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9499, 'crossentropy': 0.3882906982421875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9257069230079651})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5041334629058838})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.482867568731308})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3703569173812866})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34966009855270386})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3850249648094177})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35987570881843567})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3819078505039215})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [44071, 29110, 43083, 30699, 58575, 45451, 22436, 27877, 59477, 24173], 'labels': [-1, -1, -1, 0, -1, -1, 0, -1, -1, -1], 'scores': [0.6056323051452637, 0.406339168548584, 0.5095326900482178, 0.2955394387245178, 0.47761547565460205, 0.4250327944755554, 0.6859676241874695, 0.3937753438949585, 0.43168652057647705, 0.5054938197135925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.863682746887207})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4931592047214508})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.49360984563827515})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4358667731285095})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4444170594215393})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4686180353164673})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47667282819747925})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.37867705078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8814702033996582})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5037893056869507})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4227420389652252})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4008226990699768})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3614301383495331})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37928441166877747})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [42746, 32276, 23946, 3719, 18322, 18690, 17795, 6574, 26635, 36262], 'labels': [2, 3, -1, 2, 7, -1, 7, -1, 2, -1], 'scores': [0.49917346239089966, 0.4682711362838745, 0.37375593185424805, 0.49090132117271423, 0.4138129949569702, 0.44651418924331665, 0.4498448371887207, 0.5086172223091125, 0.54937344789505, 0.4337337017059326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8778948187828064})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5509370565414429})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46343839168548584})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5166842937469482})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4930119514465332})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5203904509544373})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9409, 'crossentropy': 0.41806279296875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8793132305145264})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44378960132598877})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4039207696914673})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40091267228126526})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3924218714237213})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [52272, 14955, 40622, 17529, 521, 29609, 39363, 38766, 38497, 56586], 'labels': [3, 5, 2, 9, -1, 1, 0, -1, 0, 5], 'scores': [0.411682665348053, 0.4280318021774292, 0.4384452700614929, 0.46190929412841797, 0.3781474828720093, 0.35529035329818726, 0.3636622428894043, 0.2948329448699951, 0.45749402046203613, 0.35787737369537354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0007083415985107})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.501237154006958})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41648542881011963})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4077954888343811})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4333077073097229})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.408706396818161})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4610203206539154})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.3578166015625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7573329210281372})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5095324516296387})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4125566780567169})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3988032639026642})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.40196096897125244})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3661367893218994})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [31310, 36008, 7378, 2290, 5394, 49624, 1239, 9516, 20166, 50274], 'labels': [0, -1, -1, -1, 8, 6, 8, 3, -1, 8], 'scores': [0.48239386081695557, 0.4538235664367676, 0.22829890251159668, 0.3835427761077881, 0.33255434036254883, 0.6058192849159241, 0.5164232850074768, 0.3803972005844116, 0.3972945213317871, 0.5046901106834412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.0773398876190186})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47634267807006836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4622191786766052})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42575496435165405})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4419841766357422})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4783862829208374})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4193241596221924})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4219621419906616})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5431228876113892})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4749525189399719})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9517, 'crossentropy': 0.3777011962890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8353447914123535})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4789731502532959})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3872673511505127})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3693804144859314})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3363635241985321})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3411839008331299})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3221520781517029})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.33149680495262146})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.30565184354782104})
store['active_learning_steps'][34]['eval_training']['best_epoch']=9
store['active_learning_steps'][34]['acquisition']={'indices': [27883, 35804, 17396, 39974, 59514, 17271, 57486, 28469, 23350, 43181], 'labels': [2, 9, -1, -1, -1, -1, -1, 5, 8, -1], 'scores': [0.38571053743362427, 0.4369223415851593, 0.3799412250518799, 0.48593127727508545, 0.3459182381629944, 0.46582353115081787, 0.3817317485809326, 0.45565739274024963, 0.5430417060852051, 0.35184037685394287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.068786859512329})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5359194278717041})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4297063946723938})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.415519654750824})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42679065465927124})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41256585717201233})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4175938367843628})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46449053287506104})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4241741895675659})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.3498431640625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7244569063186646})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47649911046028137})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4257810711860657})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38306987285614014})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35229504108428955})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3141830563545227})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3247678577899933})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.32120829820632935})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [27521, 25546, 26733, 34144, 50945, 11515, 14573, 18419, 41568, 41802], 'labels': [-1, 8, 2, -1, -1, -1, -1, -1, -1, 2], 'scores': [0.3780443072319031, 0.46418488025665283, 0.6784833669662476, 0.4842953681945801, 0.3319284915924072, 0.46225327253341675, 0.33061158657073975, 0.4929726719856262, 0.4191303253173828, 0.4237692654132843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9950202107429504})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5317907333374023})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4659802317619324})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42949068546295166})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4458182752132416})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5024268627166748})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.437914103269577})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.375331201171875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7830440402030945})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5243645906448364})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4434065520763397})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3830605149269104})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3600584864616394})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.33790844678878784})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [3290, 24238, 44591, 49893, 34077, 25321, 53464, 21492, 4822, 42658], 'labels': [4, 2, -1, 3, -1, 8, -1, -1, 4, 0], 'scores': [0.43510353565216064, 0.38766059279441833, 0.32964539527893066, 0.4522385001182556, 0.37103354930877686, 0.4130263924598694, 0.395352840423584, 0.2646833062171936, 0.5473746657371521, 0.3057578206062317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1911273002624512})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6012610793113708})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46566009521484375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4434719979763031})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4606226086616516})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3601614832878113})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4388415217399597})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42848914861679077})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4670249819755554})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9563, 'crossentropy': 0.32416142578125}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8116780519485474})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.505068302154541})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4058656096458435})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3871728777885437})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33441615104675293})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3353518545627594})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28594064712524414})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30382511019706726})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [22824, 52033, 13577, 42817, 22574, 26658, 53054, 49890, 28358, 3216], 'labels': [9, -1, -1, -1, -1, 2, -1, 5, -1, 5], 'scores': [0.45313018560409546, 0.4611719846725464, 0.398601770401001, 0.5289086103439331, 0.3963300585746765, 0.469909131526947, 0.48254525661468506, 0.5806644558906555, 0.336248517036438, 0.40979886054992676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9601783752441406})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5254635810852051})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.449459046125412})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4484078586101532})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4557609558105469})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.47907936573028564})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49132466316223145})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9416, 'crossentropy': 0.393776318359375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.847426176071167})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5604339838027954})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4443204998970032})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4169839918613434})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.38648852705955505})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.38750892877578735})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [40654, 40208, 39386, 22634, 50968, 39668, 23812, 21392, 55556, 14100], 'labels': [5, -1, 4, 0, -1, 8, 3, -1, 0, 5], 'scores': [0.5541909337043762, 0.3445601463317871, 0.485346257686615, 0.5029646158218384, 0.2852236032485962, 0.37155765295028687, 0.39183592796325684, 0.40548205375671387, 0.6554980278015137, 0.4520496726036072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0100898742675781})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5331219434738159})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4267699718475342})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4073956310749054})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38051894307136536})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3887594938278198})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42237526178359985})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37477415800094604})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38641712069511414})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3963530361652374})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4913488030433655})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9557, 'crossentropy': 0.3515821044921875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8072222471237183})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5286259055137634})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4241267442703247})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34739989042282104})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3301073908805847})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3159666061401367})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2830946445465088})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28813520073890686})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3105256259441376})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2661677896976471})
store['active_learning_steps'][39]['eval_training']['best_epoch']=10
store['active_learning_steps'][39]['acquisition']={'indices': [43379, 42042, 17712, 28460, 36238, 40487, 11195, 45081, 11186, 8932], 'labels': [-1, 4, -1, -1, 7, 9, -1, -1, -1, 0], 'scores': [0.5095910429954529, 0.5151920318603516, 0.354883074760437, 0.4638965129852295, 0.4919612407684326, 0.5631632208824158, 0.5093998908996582, 0.4119999408721924, 0.41598016023635864, 0.616366982460022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.007109522819519})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5393705368041992})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3915506601333618})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38862383365631104})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3779335021972656})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3907163441181183})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40133345127105713})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4237912893295288})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.332241357421875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8226867318153381})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4836619794368744})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38536524772644043})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3575481176376343})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.351413369178772})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34813427925109863})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34669995307922363})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [21671, 42322, 34542, 16180, 38549, 49969, 55561, 6667, 51230, 45207], 'labels': [-1, -1, 1, -1, 3, -1, -1, -1, 3, -1], 'scores': [0.3397681713104248, 0.31416773796081543, 0.430634081363678, 0.49059414863586426, 0.4141353964805603, 0.2234886884689331, 0.3699353337287903, 0.24616265296936035, 0.3577576279640198, 0.4736253619194031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0159311294555664})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5310056209564209})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4320176839828491})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3742470145225525})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38167285919189453})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40415826439857483})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38201987743377686})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9524, 'crossentropy': 0.3454978759765625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8592514991760254})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5170267224311829})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4287950396537781})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42036664485931396})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3615173399448395})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3766958713531494})
store['active_learning_steps'][41]['eval_training']['best_epoch']=5
store['active_learning_steps'][41]['acquisition']={'indices': [6011, 12581, 1030, 24404, 49400, 23012, 39411, 20225, 50021, 11949], 'labels': [-1, 4, 4, 8, -1, -1, 2, -1, 7, -1], 'scores': [0.49527692794799805, 0.4927522540092468, 0.42339062690734863, 0.27383291721343994, 0.3891095519065857, 0.48357629776000977, 0.45558613538742065, 0.3096274733543396, 0.2061101198196411, 0.4173870086669922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1716797351837158})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6165431141853333})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4438247084617615})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41849231719970703})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4159472584724426})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40908461809158325})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4124959111213684})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40741467475891113})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44221484661102295})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42782482504844666})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4160948097705841})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.3222734375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8442026376724243})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47654587030410767})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4163336753845215})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35434842109680176})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32258808612823486})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.331109881401062})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3157619833946228})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3024587035179138})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3193449378013611})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2799508273601532})
store['active_learning_steps'][42]['eval_training']['best_epoch']=10
store['active_learning_steps'][42]['acquisition']={'indices': [10886, 43780, 360, 854, 34101, 6011, 21824, 16523, 2674, 24132], 'labels': [1, -1, -1, 2, 4, -1, -1, -1, -1, -1], 'scores': [0.5893475413322449, 0.4496954679489136, 0.5254992246627808, 0.6295984983444214, 0.6099335551261902, 0.4505608081817627, 0.39788246154785156, 0.574309229850769, 0.47680509090423584, 0.49866145849227905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.136977195739746})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5821791887283325})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4390084445476532})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34808629751205444})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4080650210380554})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4122495651245117})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37642714381217957})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.344465478515625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9429575800895691})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5517021417617798})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4809049367904663})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39737093448638916})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4023592472076416})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3670268654823303})
store['active_learning_steps'][43]['eval_training']['best_epoch']=6
store['active_learning_steps'][43]['acquisition']={'indices': [33010, 26667, 42638, 4564, 2029, 55727, 11304, 1276, 52140, 6386], 'labels': [6, -1, 4, -1, 3, 0, 0, 5, 4, -1], 'scores': [0.46241670846939087, 0.16038107872009277, 0.3591451644897461, 0.547562837600708, 0.26797330379486084, 0.49923187494277954, 0.37137478590011597, 0.5971214175224304, 0.4850269556045532, 0.4079657793045044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0266399383544922})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5494531393051147})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3992062211036682})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3958280682563782})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43259376287460327})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35313963890075684})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36718684434890747})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4670960009098053})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38770145177841187})
store['active_learning_steps'][44]['training']['best_epoch']=6
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.309985986328125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8692706823348999})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.527640700340271})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4295850396156311})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38885533809661865})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3228965997695923})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30202823877334595})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2807691693305969})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3067687749862671})
store['active_learning_steps'][44]['eval_training']['best_epoch']=7
store['active_learning_steps'][44]['acquisition']={'indices': [38307, 48688, 12797, 11518, 32756, 49044, 34532, 1149, 27083, 23642], 'labels': [-1, -1, -1, -1, -1, -1, 2, 4, -1, 2], 'scores': [0.32786858081817627, 0.5112982988357544, 0.40617239475250244, 0.40126097202301025, 0.3052448034286499, 0.3579831123352051, 0.5169970393180847, 0.5305325984954834, 0.48441022634506226, 0.6022360920906067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0075671672821045})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5189019441604614})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37735435366630554})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3607293367385864})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34661316871643066})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3276125192642212})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3524949550628662})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33382540941238403})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3312453627586365})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.28961337890625}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8767596483230591})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4904305934906006})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38372620940208435})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36497777700424194})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3427926003932953})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3514916002750397})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31626805663108826})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29546788334846497})
store['active_learning_steps'][45]['eval_training']['best_epoch']=8
store['active_learning_steps'][45]['acquisition']={'indices': [51104, 26206, 36370, 15600, 47260, 644, 21019, 3273, 23138, 52479], 'labels': [8, 5, 9, -1, 6, 7, -1, -1, 2, -1], 'scores': [0.3712828755378723, 0.34957218170166016, 0.4467071294784546, 0.3386427164077759, 0.356584370136261, 0.45143377780914307, 0.4390057325363159, 0.4905310869216919, 0.3543597459793091, 0.30851173400878906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1157891750335693})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5145226716995239})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4046158194541931})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4483851194381714})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34776028990745544})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3656271696090698})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32974836230278015})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.37160009145736694})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3998689651489258})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41200095415115356})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.3047608154296875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8586056232452393})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44439274072647095})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39115557074546814})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3254092335700989})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3085968494415283})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30456674098968506})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26714950799942017})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29286280274391174})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2520867586135864})
store['active_learning_steps'][46]['eval_training']['best_epoch']=9
store['active_learning_steps'][46]['acquisition']={'indices': [57276, 4694, 50046, 391, 34378, 14096, 22006, 11734, 51234, 40081], 'labels': [8, 3, 7, 2, 7, 5, -1, 8, 5, -1], 'scores': [0.5537543892860413, 0.4635831117630005, 0.27476462721824646, 0.39098310470581055, 0.6860700249671936, 0.6170077323913574, 0.3847507834434509, 0.50429368019104, 0.6045204401016235, 0.28546297550201416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0381165742874146})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5410615801811218})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3949090242385864})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35758715867996216})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.342376708984375})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37006670236587524})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3193114399909973})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37675905227661133})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3934137225151062})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32073974609375})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9607, 'crossentropy': 0.293496337890625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8277544379234314})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4683488607406616})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3653992712497711})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3312417268753052})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32087284326553345})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3254409432411194})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3014514446258545})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2861207127571106})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28746116161346436})
store['active_learning_steps'][47]['eval_training']['best_epoch']=8
store['active_learning_steps'][47]['acquisition']={'indices': [21900, 31192, 32328, 5238, 37465, 33594, 1872, 7829, 56457, 17079], 'labels': [6, -1, -1, 3, 5, 3, 3, -1, 3, 6], 'scores': [0.495179682970047, 0.33823108673095703, 0.4320640563964844, 0.4388543963432312, 0.578010618686676, 0.36319971084594727, 0.3828197121620178, 0.5809639096260071, 0.6059033870697021, 0.23938816785812378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.979568600654602})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5545580983161926})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3777463436126709})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36300426721572876})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32573407888412476})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34471458196640015})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35968488454818726})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36620038747787476})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.2794214111328125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8683450818061829})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5094974040985107})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4107328951358795})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37603726983070374})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3676280379295349})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3380774259567261})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32060280442237854})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [29165, 50698, 19782, 49217, 49082, 54933, 39806, 38760, 16990, 12178], 'labels': [-1, 9, 1, 8, 3, 6, 8, 9, -1, -1], 'scores': [0.29117125272750854, 0.3631913661956787, 0.42364585399627686, 0.4692566990852356, 0.318661093711853, 0.5843545198440552, 0.3195171356201172, 0.38214969635009766, 0.32806265354156494, 0.3950779438018799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1708391904830933})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6230912208557129})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3758414387702942})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34714579582214355})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3454345166683197})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38655245304107666})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.395663321018219})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39330989122390747})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.2810193603515625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8100342154502869})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.48205238580703735})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4382038116455078})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3198642134666443})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3350306451320648})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34677132964134216})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3174455761909485})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [42838, 24196, 49198, 20614, 34583, 20069, 40823, 13528, 22065, 40857], 'labels': [9, -1, 1, 8, 7, -1, -1, 0, -1, -1], 'scores': [0.5804974436759949, 0.6407066583633423, 0.4834163188934326, 0.21365147829055786, 0.4968690276145935, 0.3179202079772949, 0.2214055061340332, 0.43045270442962646, 0.44400012493133545, 0.35439109802246094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0215332508087158})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5254788398742676})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39767777919769287})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3632112741470337})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32202208042144775})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3414008617401123})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3158356547355652})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3308812975883484})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34976786375045776})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33460190892219543})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.276383203125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9009321331977844})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5340785980224609})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39247947931289673})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3758569657802582})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33799853920936584})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30787330865859985})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30712026357650757})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2957307696342468})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27772989869117737})
store['active_learning_steps'][50]['eval_training']['best_epoch']=9
store['active_learning_steps'][50]['acquisition']={'indices': [33763, 42240, 33847, 15796, 32488, 8409, 54294, 31054, 46730, 14116], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3608776926994324, 0.42070508003234863, 0.5777024030685425, 0.5408090949058533, 0.48897993564605713, 0.5467175841331482, 0.44898760318756104, 0.35217106342315674, 0.3574753999710083, 0.28387343883514404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0871249437332153})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5948832035064697})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41985541582107544})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37130361795425415})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4009862244129181})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37811219692230225})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3640452027320862})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34696847200393677})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3536405563354492})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38309216499328613})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35703036189079285})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.3110872314453125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9460911750793457})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.535855770111084})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3990051746368408})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3377615213394165})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31711333990097046})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3142262101173401})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27400314807891846})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2967066764831543})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2793905735015869})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2479982227087021})
store['active_learning_steps'][51]['eval_training']['best_epoch']=10
store['active_learning_steps'][51]['acquisition']={'indices': [47247, 43212, 10256, 58007, 56292, 36350, 13920, 14385, 39835, 29501], 'labels': [0, 5, 2, -1, 9, -1, -1, 8, 7, -1], 'scores': [0.5526561737060547, 0.5068584680557251, 0.5013624429702759, 0.3081783056259155, 0.48884332180023193, 0.36480486392974854, 0.3292059898376465, 0.45191076397895813, 0.3825426995754242, 0.4298035502433777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.129763126373291})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5147572755813599})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38061004877090454})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36046290397644043})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33763018250465393})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32016634941101074})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3608185946941376})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32742613554000854})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33807241916656494})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.270873681640625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.891680896282196})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5620152354240417})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42228391766548157})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35747024416923523})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31671062111854553})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3108031451702118})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2901036739349365})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2849184274673462})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [53478, 13462, 19702, 36072, 17481, 51194, 41998, 41289, 7029, 51842], 'labels': [7, -1, 5, 2, -1, 9, 7, -1, 2, 9], 'scores': [0.35866135358810425, 0.39348113536834717, 0.48028022050857544, 0.6270886659622192, 0.3781377077102661, 0.4258701801300049, 0.3771023452281952, 0.5212318897247314, 0.44259119033813477, 0.43949174880981445]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2252572774887085})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6007359623908997})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4570158123970032})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3960961699485779})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3739224672317505})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37206074595451355})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4072076082229614})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41164499521255493})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3512670397758484})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4077579975128174})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3845977187156677})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38226720690727234})
store['active_learning_steps'][53]['training']['best_epoch']=9
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.3056520751953125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.873871922492981})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4969104528427124})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35313665866851807})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31405776739120483})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32551801204681396})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28646373748779297})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3193114995956421})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.27735891938209534})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28572332859039307})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27008429169654846})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2573471665382385})
store['active_learning_steps'][53]['eval_training']['best_epoch']=11
store['active_learning_steps'][53]['acquisition']={'indices': [29764, 10156, 37722, 53873, 58829, 7083, 59314, 31787, 59283, 6366], 'labels': [4, 1, -1, 4, 0, 4, 9, -1, 4, -1], 'scores': [0.45006901025772095, 0.412675678730011, 0.5409464836120605, 0.4949589967727661, 0.5948259234428406, 0.5886639952659607, 0.6242596507072449, 0.3997840881347656, 0.578750729560852, 0.37215447425842285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0582385063171387})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5294700860977173})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.403369665145874})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3533036708831787})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34950369596481323})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3869748115539551})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3802555203437805})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34826943278312683})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35143837332725525})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3662651777267456})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3547857999801636})
store['active_learning_steps'][54]['training']['best_epoch']=8
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.284815380859375}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9475345611572266})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5249556303024292})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3995881676673889})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35490208864212036})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33068445324897766})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3141539394855499})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2818572223186493})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3060687780380249})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2618161737918854})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25124111771583557})
store['active_learning_steps'][54]['eval_training']['best_epoch']=10
store['active_learning_steps'][54]['acquisition']={'indices': [14647, 3582, 57955, 53464, 24014, 55651, 28694, 33157, 7248, 12394], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.37309032678604126, 0.4532134532928467, 0.22533798217773438, 0.40451550483703613, 0.5959481596946716, 0.30595219135284424, 0.30121201276779175, 0.3329129219055176, 0.41262221336364746, 0.3779228925704956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.097684383392334})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6278308629989624})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3766421675682068})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37721139192581177})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3698637783527374})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3235512971878052})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35829171538352966})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3723195791244507})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34091150760650635})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.294925439453125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8450156450271606})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4866412878036499})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36521559953689575})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3226470351219177})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3246777653694153})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3123423755168915})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29717445373535156})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29648157954216003})
store['active_learning_steps'][55]['eval_training']['best_epoch']=8
store['active_learning_steps'][55]['acquisition']={'indices': [8491, 11482, 47160, 57999, 36267, 10756, 39714, 42777, 55304, 41799], 'labels': [1, 8, -1, -1, -1, 3, -1, -1, -1, -1], 'scores': [0.3667212724685669, 0.6063764095306396, 0.4052886962890625, 0.3855321407318115, 0.48543107509613037, 0.48863327503204346, 0.33712172508239746, 0.5074005126953125, 0.5049631595611572, 0.3978925943374634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.082019567489624})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5436785221099854})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3691948354244232})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37246888875961304})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3221435546875})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32331937551498413})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.338115394115448})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35129988193511963})
store['active_learning_steps'][56]['training']['best_epoch']=5
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.2747769775390625}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9640331268310547})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5090646147727966})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42025166749954224})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3785261809825897})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3533097505569458})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3251160681247711})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3111054003238678})
store['active_learning_steps'][56]['eval_training']['best_epoch']=7
store['active_learning_steps'][56]['acquisition']={'indices': [22767, 42153, 25604, 40644, 31200, 28746, 11364, 25246, 21164, 37758], 'labels': [3, 0, 4, 1, 9, -1, 2, 2, 2, 0], 'scores': [0.26800209283828735, 0.4283210039138794, 0.25969886779785156, 0.3223867118358612, 0.31455206871032715, 0.4561973810195923, 0.47811639308929443, 0.41305243968963623, 0.45258641242980957, 0.4537503719329834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1489336490631104})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49221694469451904})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36793744564056396})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.340078741312027})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30649495124816895})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31715041399002075})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3171495199203491})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31411266326904297})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2634442138671875}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8668811321258545})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5402992367744446})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4271686375141144})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40665847063064575})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.340527206659317})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3423621654510498})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33581680059432983})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [58626, 38415, 52225, 49292, 4198, 45048, 53927, 17545, 42491, 9057], 'labels': [6, -1, 2, -1, -1, 4, -1, -1, 2, -1], 'scores': [0.3071732521057129, 0.4063260555267334, 0.48826879262924194, 0.39182066917419434, 0.32435691356658936, 0.4493641257286072, 0.42611217498779297, 0.274324893951416, 0.4933585524559021, 0.3492591381072998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.150604486465454})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5307774543762207})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4079097509384155})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34883373975753784})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3591502904891968})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32221394777297974})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3269558250904083})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33561989665031433})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3036593198776245})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34444862604141235})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36455655097961426})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3563860058784485})
store['active_learning_steps'][58]['training']['best_epoch']=9
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.274287109375}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9793881177902222})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.536213755607605})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3844687044620514})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3360757827758789})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3159230649471283})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34161072969436646})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2937778830528259})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2738731801509857})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28124722838401794})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2672772705554962})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2857193350791931})
store['active_learning_steps'][58]['eval_training']['best_epoch']=10
store['active_learning_steps'][58]['acquisition']={'indices': [7259, 45185, 43248, 14313, 32880, 22716, 12663, 15779, 4634, 55564], 'labels': [2, 7, 9, -1, 0, -1, 8, 0, 8, -1], 'scores': [0.3508022427558899, 0.4506412744522095, 0.4380919635295868, 0.41605710983276367, 0.5419172644615173, 0.37368643283843994, 0.7063015699386597, 0.7115723490715027, 0.6039063334465027, 0.3379364013671875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0718083381652832})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5066173076629639})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39076465368270874})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3208630084991455})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3388725817203522})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3306954503059387})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.335629940032959})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.298259423828125}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9594064950942993})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5385702252388})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4111284017562866})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36958491802215576})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3344617486000061})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3576263189315796})
store['active_learning_steps'][59]['eval_training']['best_epoch']=5
store['active_learning_steps'][59]['acquisition']={'indices': [27455, 30063, 38000, 58157, 24292, 37583, 39865, 3360, 55490, 48717], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, -1, -1], 'scores': [0.4542732238769531, 0.3435078263282776, 0.3126945495605469, 0.3870052695274353, 0.3896127939224243, 0.38029754161834717, 0.43127572536468506, 0.372900128364563, 0.40690183639526367, 0.40169692039489746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0727683305740356})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.521659255027771})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40347957611083984})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35796552896499634})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3542909324169159})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3514694571495056})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.309431791305542})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3247271776199341})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3516860604286194})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3755932152271271})
store['active_learning_steps'][60]['training']['best_epoch']=7
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.2787927978515625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0012507438659668})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49958372116088867})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4241971969604492})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3949079215526581})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3398285508155823})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32917261123657227})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29683518409729004})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29366517066955566})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2679672837257385})
store['active_learning_steps'][60]['eval_training']['best_epoch']=9
store['active_learning_steps'][60]['acquisition']={'indices': [51236, 24200, 21876, 33412, 17264, 5553, 18879, 25243, 57394, 48134], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5441452860832214, 0.30970561504364014, 0.41005635261535645, 0.46286946535110474, 0.22246891260147095, 0.6393193602561951, 0.5067504644393921, 0.35016918182373047, 0.287070095539093, 0.2702958583831787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2696171998977661})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6223709583282471})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3902287185192108})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34090322256088257})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33953171968460083})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34778231382369995})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3020283877849579})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36834612488746643})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35485684871673584})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.352861225605011})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2552504638671875}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9093763828277588})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.543367326259613})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39011862874031067})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3307536840438843})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3020903766155243})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31271883845329285})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2894446849822998})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27963581681251526})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2837432026863098})
store['active_learning_steps'][61]['eval_training']['best_epoch']=8
store['active_learning_steps'][61]['acquisition']={'indices': [25719, 15225, 43544, 38779, 52889, 7204, 24969, 45056, 38318, 46724], 'labels': [-1, -1, 9, -1, -1, -1, -1, 8, -1, 7], 'scores': [0.3389929533004761, 0.4429436922073364, 0.4899730086326599, 0.3579646348953247, 0.7049251794815063, 0.3510158061981201, 0.33682072162628174, 0.47464901208877563, 0.5627407431602478, 0.5564518570899963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1262602806091309})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5173007845878601})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4318530559539795})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33848416805267334})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33502113819122314})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2871830463409424})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31306058168411255})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3194105923175812})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30532240867614746})
store['active_learning_steps'][62]['training']['best_epoch']=6
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.25459482421875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.915425181388855})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5131145119667053})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39140355587005615})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3388470411300659})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3350074589252472})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3267925977706909})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3152347207069397})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29053255915641785})
store['active_learning_steps'][62]['eval_training']['best_epoch']=8
store['active_learning_steps'][62]['acquisition']={'indices': [23086, 30533, 29056, 26705, 23463, 27540, 16738, 15174, 17119, 17222], 'labels': [8, -1, -1, 7, -1, 3, -1, -1, -1, 8], 'scores': [0.443355917930603, 0.318947434425354, 0.35544002056121826, 0.2613559067249298, 0.3725306987762451, 0.2990327477455139, 0.28227102756500244, 0.39837050437927246, 0.2746901512145996, 0.43928563594818115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9796514511108398})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5946329832077026})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41212984919548035})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3525475859642029})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34491828083992004})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31943708658218384})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3017783463001251})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3136473000049591})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3105631470680237})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31026095151901245})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.2584037109375}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9143654108047485})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.516043484210968})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38605305552482605})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35017460584640503})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3309614956378937})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30975669622421265})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2825627326965332})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2839793860912323})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28965914249420166})
store['active_learning_steps'][63]['eval_training']['best_epoch']=7
store['active_learning_steps'][63]['acquisition']={'indices': [8946, 24915, 10763, 23083, 46894, 34359, 39458, 1564, 18003, 19324], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.246232271194458, 0.2653120756149292, 0.4553251266479492, 0.42780542373657227, 0.3238319158554077, 0.5155901908874512, 0.3236119747161865, 0.4553391933441162, -0.2808777391910553, 0.3722860813140869]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.172699213027954})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5924069881439209})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.42455828189849854})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3651888966560364})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3208998441696167})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3084809184074402})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32812148332595825})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.318087637424469})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3152390718460083})
store['active_learning_steps'][64]['training']['best_epoch']=6
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.282754931640625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.012495756149292})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5158572196960449})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4296453893184662})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37914884090423584})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3123769760131836})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3581036627292633})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31151241064071655})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3095095157623291})
store['active_learning_steps'][64]['eval_training']['best_epoch']=8
store['active_learning_steps'][64]['acquisition']={'indices': [2956, 59128, 32207, 466, 25721, 50732, 57242, 57758, 42504, 20169], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, 8, 4], 'scores': [0.4018481969833374, 0.24192190170288086, 0.3344219923019409, 0.3301776647567749, 0.39879417419433594, 0.4245002269744873, 0.43773889541625977, 0.3449063301086426, 0.5024933218955994, 0.5373116731643677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.118424654006958})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.610919713973999})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3940005898475647})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34700366854667664})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32438623905181885})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37716996669769287})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3290221095085144})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35104528069496155})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2768563232421875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9626568555831909})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5690367221832275})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4463627338409424})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36455732583999634})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3469446897506714})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35495471954345703})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.333498477935791})
store['active_learning_steps'][65]['eval_training']['best_epoch']=7
store['active_learning_steps'][65]['acquisition']={'indices': [52197, 28368, 23845, 5303, 10915, 49910, 14251, 26952, 25243, 18924], 'labels': [6, 9, -1, -1, -1, 6, -1, -1, -1, 3], 'scores': [0.4793996810913086, 0.6302947998046875, 0.3656158447265625, 0.35323506593704224, 0.4033907651901245, 0.4425317645072937, 0.3978976011276245, 0.4051327705383301, 0.34421324729919434, 0.6379245519638062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.304593801498413})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6188989281654358})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4053983688354492})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3328518867492676})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.357524573802948})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3176268935203552})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3303358554840088})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32265666127204895})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3138774037361145})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3077089786529541})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30921611189842224})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3185189962387085})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3116486668586731})
store['active_learning_steps'][66]['training']['best_epoch']=10
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2690541015625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.001326322555542})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6290550231933594})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41552865505218506})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34200307726860046})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31916195154190063})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34584105014801025})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.309237003326416})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29893094301223755})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.269987016916275})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2708095908164978})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.283988893032074})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27347230911254883})
store['active_learning_steps'][66]['eval_training']['best_epoch']=9
store['active_learning_steps'][66]['acquisition']={'indices': [27583, 30002, 5035, 11014, 21100, 26192, 50241, 6070, 46432, 56808], 'labels': [-1, -1, 7, -1, -1, -1, -1, -1, 6, 4], 'scores': [0.26020610332489014, 0.4190569519996643, 0.4370906352996826, 0.5063825845718384, 0.41473913192749023, 0.5577288269996643, 0.3958258032798767, 0.33537256717681885, 0.3924940824508667, 0.34836822748184204]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1220730543136597})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6095137596130371})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42205554246902466})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.364316463470459})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3685210347175598})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3000723123550415})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38871076703071594})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.314456045627594})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.355873167514801})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.270620556640625}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8879191875457764})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49201804399490356})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4135313034057617})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35857445001602173})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.360232949256897})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3346574902534485})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26572734117507935})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27112698554992676})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [18386, 101, 46899, 6319, 3629, 30328, 49187, 58047, 42498, 40943], 'labels': [-1, -1, 3, 7, -1, -1, 7, -1, -1, -1], 'scores': [0.2291043996810913, 0.39693915843963623, 0.4144498109817505, 0.32146286964416504, 0.35701990127563477, 0.37702834606170654, 0.4211219549179077, 0.45201873779296875, 0.49623429775238037, 0.39126408100128174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0342594385147095})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5145106315612793})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3836759030818939})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3162291944026947})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.333079069852829})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3038034439086914})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29730117321014404})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34718024730682373})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2861754298210144})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3365631103515625})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29656267166137695})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3094557225704193})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.252409228515625}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9242019057273865})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5204403400421143})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.387409508228302})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3657290041446686})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34457284212112427})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26680833101272583})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3049601912498474})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28233402967453003})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2687302231788635})
store['active_learning_steps'][68]['eval_training']['best_epoch']=6
store['active_learning_steps'][68]['acquisition']={'indices': [49875, 41650, 22808, 39315, 51356, 28128, 55899, 30266, 11546, 1254], 'labels': [-1, -1, -1, -1, -1, 4, -1, 4, -1, -1], 'scores': [0.425986647605896, 0.3224126696586609, 0.32398557662963867, 0.33652257919311523, 0.39082133769989014, 0.3266659080982208, 0.23231196403503418, 0.5123250186443329, 0.32774603366851807, 0.43306440114974976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2506306171417236})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5418473482131958})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4136345386505127})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3852192163467407})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3362829089164734})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32064834237098694})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3196673095226288})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30283278226852417})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31757235527038574})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3191605806350708})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3064343333244324})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2754415771484375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8598039150238037})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5048311948776245})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3406541645526886})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34169965982437134})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29357588291168213})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29103684425354004})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3121224045753479})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3058651089668274})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26169753074645996})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2607506513595581})
store['active_learning_steps'][69]['eval_training']['best_epoch']=10
store['active_learning_steps'][69]['acquisition']={'indices': [32747, 10516, 50039, 4785, 10310, 9476, 1339, 8093, 9208, 31238], 'labels': [8, -1, -1, -1, -1, -1, -1, 0, 8, -1], 'scores': [0.5321319103240967, 0.3780210614204407, 0.49615252017974854, 0.40421628952026367, 0.6254562139511108, 0.4658924341201782, 0.5963827967643738, 0.6441172957420349, 0.5865287780761719, 0.5151546597480774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.240390419960022})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5680294036865234})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4032898247241974})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3599405884742737})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3205782175064087})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30687597393989563})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2689591646194458})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2657667398452759})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2862672805786133})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26429086923599243})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29135870933532715})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2842738926410675})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30503448843955994})
store['active_learning_steps'][70]['training']['best_epoch']=10
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.2446529296875}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8057737350463867})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4727579653263092})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39090609550476074})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.314721941947937})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26210731267929077})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2923406660556793})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2620362639427185})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26620054244995117})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27171754837036133})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21875546872615814})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23583513498306274})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24648772180080414})
store['active_learning_steps'][70]['eval_training']['best_epoch']=10
store['active_learning_steps'][70]['acquisition']={'indices': [54629, 40690, 45318, 2632, 2740, 5647, 56488, 14700, 34620, 36107], 'labels': [-1, -1, -1, -1, -1, -1, 3, -1, -1, -1], 'scores': [0.5605889558792114, 0.42162394523620605, 0.6044808626174927, 0.6933421492576599, 0.4433647394180298, 0.3153804540634155, 0.6967954039573669, 0.5132201313972473, 0.34938305616378784, 0.33331114053726196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1298415660858154})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5793783664703369})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4525621831417084})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36597752571105957})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31924575567245483})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3443109393119812})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3326798975467682})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3127181828022003})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3415493965148926})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32390064001083374})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33390146493911743})
store['active_learning_steps'][71]['training']['best_epoch']=8
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.27404169921875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9614300727844238})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5609588623046875})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3876480460166931})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35773593187332153})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30506062507629395})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3224233388900757})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2983303666114807})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26299914717674255})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2735675573348999})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2924065589904785})
store['active_learning_steps'][71]['eval_training']['best_epoch']=8
store['active_learning_steps'][71]['acquisition']={'indices': [46088, 55021, 52464, 15545, 25883, 14439, 49851, 23239, 25125, 12397], 'labels': [6, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.604679524898529, 0.4546019434928894, 0.4881705641746521, 0.454902708530426, 0.24765682220458984, 0.576435923576355, 0.4404321312904358, 0.4011542797088623, 0.5702428817749023, 0.27499938011169434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2735576629638672})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6447699069976807})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44156062602996826})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3493387699127197})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3080923557281494})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3095585107803345})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3353201746940613})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34150952100753784})
store['active_learning_steps'][72]['training']['best_epoch']=5
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.2894891357421875}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9251258373260498})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5326476097106934})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40336012840270996})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39934420585632324})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.40768536925315857})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.313619464635849})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3198600709438324})
store['active_learning_steps'][72]['eval_training']['best_epoch']=6
store['active_learning_steps'][72]['acquisition']={'indices': [14275, 55384, 3010, 17469, 38912, 49012, 47949, 17552, 16219, 2426], 'labels': [-1, -1, 7, -1, -1, 7, 5, -1, 5, 1], 'scores': [0.25109195709228516, 0.31216633319854736, 0.3432178497314453, 0.46435558795928955, 0.5716836452484131, 0.3157232999801636, 0.45951855182647705, 0.25931525230407715, 0.4496103525161743, 0.5058803558349609]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2031776905059814})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5781244039535522})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4515970051288605})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4125581979751587})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3058801293373108})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3058129549026489})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2836490571498871})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32816487550735474})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3003060221672058})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2975015342235565})
store['active_learning_steps'][73]['training']['best_epoch']=7
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.26132177734375}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9165223240852356})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43092086911201477})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4047798216342926})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3408185541629791})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3329184651374817})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27961060404777527})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3120461106300354})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.288041889667511})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27872225642204285})
store['active_learning_steps'][73]['eval_training']['best_epoch']=9
store['active_learning_steps'][73]['acquisition']={'indices': [31389, 17924, 57154, 52092, 3118, 36878, 19942, 24740, 3034, 28392], 'labels': [-1, -1, 0, 7, 5, 8, 5, -1, -1, 3], 'scores': [0.4248429536819458, 0.5838284492492676, 0.46590733528137207, 0.5139253437519073, 0.6145467162132263, 0.3817128837108612, 0.7072838544845581, 0.4579019546508789, 0.4630732536315918, 0.5005895495414734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2745797634124756})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6077465415000916})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39789140224456787})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3403274118900299})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27534645795822144})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3435261845588684})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30584314465522766})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3261740803718567})
store['active_learning_steps'][74]['training']['best_epoch']=5
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.2913756103515625}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.949762761592865})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5884082317352295})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4602116048336029})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4120800495147705})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38670194149017334})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35774126648902893})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3843613862991333})
store['active_learning_steps'][74]['eval_training']['best_epoch']=6
store['active_learning_steps'][74]['acquisition']={'indices': [30111, 21387, 36478, 44567, 6931, 51748, 7058, 44621, 53470, 48340], 'labels': [8, -1, -1, -1, -1, 2, 3, -1, 5, -1], 'scores': [0.47354447841644287, 0.5079363584518433, 0.30108165740966797, 0.3944817781448364, 0.4026801586151123, 0.42689085006713867, 0.38643765449523926, 0.35005295276641846, 0.42870479822158813, 0.3896371126174927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1095662117004395})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5703822374343872})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38455730676651})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38392022252082825})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3037622570991516})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.294217973947525})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3436359763145447})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2945149540901184})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30402514338493347})
store['active_learning_steps'][75]['training']['best_epoch']=6
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.26430654296875}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9034818410873413})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5234219431877136})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4161112904548645})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33389121294021606})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3155696392059326})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3051648736000061})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3008195161819458})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27768242359161377})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [7352, 34645, 32934, 3206, 43011, 34913, 30830, 2546, 9708, 43758], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.4795292615890503, 0.45697033405303955, 0.4091435670852661, 0.559890627861023, 0.4056442975997925, 0.4733469486236572, 0.4579712152481079, 0.42043888568878174, 0.4299226999282837, 0.4349483251571655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2809269428253174})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6351594924926758})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3880501389503479})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3374159634113312})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3023298382759094})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34502094984054565})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27669981122016907})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28400057554244995})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2993255853652954})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28444790840148926})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.252654833984375}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9031200408935547})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49530717730522156})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.373974084854126})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33673548698425293})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3426799774169922})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2802237272262573})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3072420358657837})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25566476583480835})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2708057165145874})
store['active_learning_steps'][76]['eval_training']['best_epoch']=8
store['active_learning_steps'][76]['acquisition']={'indices': [5346, 31878, 27254, 17733, 52834, 15892, 5110, 42163, 39759, 24843], 'labels': [-1, -1, -1, -1, 2, -1, -1, -1, -1, -1], 'scores': [0.3901681900024414, 0.4172964096069336, 0.41872668266296387, 0.4258391261100769, 0.595669150352478, 0.47289061546325684, 0.2529066801071167, 0.48736053705215454, 0.46723753213882446, 0.4326920509338379]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.118168830871582})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.599623441696167})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4259856939315796})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3400817811489105})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3164854049682617})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30233120918273926})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32640165090560913})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3524671196937561})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3133714497089386})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.281263720703125}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 1.0088136196136475})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5216137766838074})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42760834097862244})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37216442823410034})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3342199921607971})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34817564487457275})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29073500633239746})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2928215563297272})
store['active_learning_steps'][77]['eval_training']['best_epoch']=7
store['active_learning_steps'][77]['acquisition']={'indices': [27855, 30350, 31748, 42529, 2151, 52385, 24777, 50486, 2137, 36149], 'labels': [-1, -1, 3, 9, -1, -1, -1, -1, 9, 3], 'scores': [0.4691723585128784, 0.39578962326049805, 0.39462077617645264, 0.4945032596588135, 0.4418962597846985, 0.22793400287628174, 0.30357420444488525, 0.25879430770874023, 0.5577437877655029, 0.42703747749328613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2011172771453857})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6009617447853088})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4708663821220398})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3633297383785248})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3418715000152588})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3152179718017578})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29325437545776367})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.299254834651947})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30788347125053406})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31268006563186646})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.27602412109375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9995666742324829})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.538263738155365})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3996255695819855})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3507460355758667})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3087421655654907})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33123189210891724})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.284041166305542})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3359953761100769})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28946515917778015})
store['active_learning_steps'][78]['eval_training']['best_epoch']=7
store['active_learning_steps'][78]['acquisition']={'indices': [59589, 46316, 50242, 34860, 43181, 14314, 22272, 47515, 2627, 39123], 'labels': [-1, 9, -1, 4, -1, 1, 5, -1, -1, 4], 'scores': [0.3823487162590027, 0.41501903533935547, 0.3852752447128296, 0.30648547410964966, 0.44018828868865967, 0.41126084327697754, 0.5946600437164307, 0.3593752384185791, 0.3961679935455322, 0.38465434312820435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2074323892593384})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5750941038131714})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3909686505794525})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3307414650917053})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27227872610092163})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2571317255496979})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30341529846191406})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30696189403533936})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30501434206962585})
store['active_learning_steps'][79]['training']['best_epoch']=6
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.25188916015625}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9800652861595154})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4884905517101288})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4066743850708008})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3654119372367859})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3370184898376465})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3183692395687103})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30864477157592773})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2918248176574707})
store['active_learning_steps'][79]['eval_training']['best_epoch']=8
store['active_learning_steps'][79]['acquisition']={'indices': [42078, 40240, 21218, 18398, 228, 53043, 26796, 40422, 3046, 24994], 'labels': [4, 0, -1, 4, 3, -1, -1, 5, -1, -1], 'scores': [0.596446692943573, 0.2804858684539795, 0.32293248176574707, 0.6444156765937805, 0.3727816939353943, 0.2659965753555298, 0.258073091506958, 0.32283803820610046, 0.2713521718978882, 0.2203284502029419]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1774485111236572})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5476163625717163})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4069218337535858})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33776402473449707})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3039987087249756})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31623345613479614})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29029029607772827})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2959740459918976})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.270871102809906})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2702574133872986})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28160274028778076})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29043614864349365})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3392407298088074})
store['active_learning_steps'][80]['training']['best_epoch']=10
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2562928955078125}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0285910367965698})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5822861790657043})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.370495080947876})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33355486392974854})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2963204085826874})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2953198552131653})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26989227533340454})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2781020998954773})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2723292112350464})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25924405455589294})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2576720416545868})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22233569622039795})
store['active_learning_steps'][80]['eval_training']['best_epoch']=12
store['active_learning_steps'][80]['acquisition']={'indices': [2699, 19040, 5591, 15701, 36478, 53252, 17019, 45553, 29168, 1307], 'labels': [-1, 6, -1, 3, -1, -1, 9, -1, -1, -1], 'scores': [0.27518773078918457, 0.34199732542037964, 0.5248895287513733, 0.4504314064979553, 0.4389312267303467, 0.42670780420303345, 0.5168856978416443, 0.49760866165161133, 0.48170214891433716, 0.43311798572540283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.215433120727539})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6155797243118286})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41716164350509644})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3386102318763733})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3191908001899719})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3000788688659668})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2928619980812073})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27534568309783936})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26197588443756104})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28530871868133545})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2718616724014282})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29535117745399475})
store['active_learning_steps'][81]['training']['best_epoch']=9
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.252840380859375}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8989059925079346})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4930154085159302})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3695427179336548})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3143215775489807})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30441343784332275})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.275001585483551})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2643199563026428})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2786807119846344})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22932890057563782})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24706372618675232})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27868354320526123})
store['active_learning_steps'][81]['eval_training']['best_epoch']=9
store['active_learning_steps'][81]['acquisition']={'indices': [48280, 12341, 23404, 37102, 16298, 8974, 50712, 15192, 36744, 57303], 'labels': [-1, -1, -1, -1, 2, -1, -1, -1, 1, -1], 'scores': [0.4544023871421814, 0.21185767650604248, 0.5453829765319824, 0.5738557577133179, 0.620394229888916, 0.5406408309936523, 0.45497405529022217, 0.479051411151886, 0.5986965298652649, 0.4924360513687134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.3513362407684326})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6850671768188477})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41335397958755493})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35245078802108765})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36304569244384766})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3324412703514099})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2970496118068695})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33601316809654236})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.318356990814209})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29750382900238037})
store['active_learning_steps'][82]['training']['best_epoch']=7
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2624615966796875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8380252122879028})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.48729199171066284})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38060569763183594})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.338225781917572})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31339573860168457})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.297913134098053})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2931551933288574})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2419007122516632})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26813098788261414})
store['active_learning_steps'][82]['eval_training']['best_epoch']=8
store['active_learning_steps'][82]['acquisition']={'indices': [57507, 25498, 50758, 30173, 36766, 29206, 26859, 30838, 48561, 32612], 'labels': [0, 4, -1, 8, 6, 4, -1, 9, -1, -1], 'scores': [0.5494297742843628, 0.4118645191192627, 0.36832988262176514, 0.4937746822834015, 0.4867839813232422, 0.47125399112701416, 0.4491118788719177, 0.5418649315834045, 0.488253116607666, 0.374906063079834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2294505834579468})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5463186502456665})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39931556582450867})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2689104378223419})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31574857234954834})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2843775451183319})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3103634715080261})
store['active_learning_steps'][83]['training']['best_epoch']=4
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2702715087890625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8859032392501831})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5763896703720093})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.4133360981941223})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3959168791770935})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3969537019729614})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.39913737773895264})
store['active_learning_steps'][83]['eval_training']['best_epoch']=4
store['active_learning_steps'][83]['acquisition']={'indices': [21794, 11195, 42894, 40398, 17871, 40976, 27492, 23407, 51808, 32393], 'labels': [-1, -1, -1, -1, -1, 1, -1, -1, -1, 5], 'scores': [0.44809389114379883, 0.3791707754135132, 0.3268927335739136, 0.44209349155426025, 0.29511260986328125, 0.4673987627029419, 0.4144015312194824, 0.3031519651412964, 0.30830657482147217, 0.4037832021713257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3191347122192383})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6066436767578125})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40619802474975586})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.36960119009017944})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3295956254005432})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2829497456550598})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3043608069419861})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2772239148616791})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2845047116279602})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27197718620300293})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30726248025894165})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.301727831363678})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2894367575645447})
store['active_learning_steps'][84]['training']['best_epoch']=10
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2514964599609375}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9919718503952026})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5479023456573486})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3914639353752136})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33403700590133667})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3193241357803345})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28989362716674805})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.309994637966156})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2825812101364136})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2824440598487854})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2508121132850647})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24390718340873718})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23439133167266846})
store['active_learning_steps'][84]['eval_training']['best_epoch']=12
store['active_learning_steps'][84]['acquisition']={'indices': [15741, 22098, 48461, 21174, 28225, 43095, 17190, 34096, 51972, 50250], 'labels': [-1, -1, -1, 2, -1, -1, 9, -1, -1, -1], 'scores': [0.4695547819137573, 0.6882307529449463, 0.4130518436431885, 0.5821546614170074, 0.41276228427886963, 0.38424646854400635, 0.4554510712623596, 0.3884294033050537, 0.4024392366409302, 0.5764316320419312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2407310009002686})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6417930722236633})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4264625906944275})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3737354278564453})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3212500214576721})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28595250844955444})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3495209217071533})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2984637916088104})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30248749256134033})
store['active_learning_steps'][85]['training']['best_epoch']=6
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.27541171875}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.9109482765197754})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5427486300468445})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41957196593284607})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37996989488601685})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32827508449554443})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33560416102409363})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31598129868507385})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3284711539745331})
store['active_learning_steps'][85]['eval_training']['best_epoch']=7
store['active_learning_steps'][85]['acquisition']={'indices': [16456, 54296, 25097, 11208, 35256, 19411, 24856, 33680, 47256, 8904], 'labels': [-1, -1, -1, 9, -1, -1, -1, -1, -1, 1], 'scores': [0.44994598627090454, 0.3241615295410156, 0.2525761127471924, 0.47713619470596313, 0.4449659585952759, 0.3670913577079773, 0.22843825817108154, 0.4068840742111206, 0.415988564491272, 0.281871497631073]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.191532850265503})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6108362674713135})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.430213063955307})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3285049796104431})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33937373757362366})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3106116056442261})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.306498646736145})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26734352111816406})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2875450849533081})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32958298921585083})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27149155735969543})
store['active_learning_steps'][86]['training']['best_epoch']=8
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.27031416015625}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0041077136993408})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.49193739891052246})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.43254703283309937})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3274117112159729})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3075304329395294})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28994932770729065})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3021059036254883})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2739037573337555})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2557055354118347})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2536680996417999})
store['active_learning_steps'][86]['eval_training']['best_epoch']=10
store['active_learning_steps'][86]['acquisition']={'indices': [18508, 5905, 40087, 27145, 7186, 38733, 29018, 32718, 58560, 15818], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1], 'scores': [0.26937514543533325, 0.38867396116256714, 0.39235198497772217, 0.316267728805542, 0.39955949783325195, 0.3775613307952881, 0.5095692873001099, 0.39728856086730957, 0.6281118094921112, 0.35185694694519043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.1891307830810547})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5258536338806152})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3645150661468506})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3102729320526123})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29368823766708374})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29073095321655273})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31072863936424255})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31440478563308716})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2866210341453552})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30686014890670776})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26107221841812134})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31072455644607544})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2953224182128906})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30685606598854065})
store['active_learning_steps'][87]['training']['best_epoch']=11
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.24816123046875}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9959098100662231})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5158226490020752})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4423471987247467})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32402586936950684})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2582944631576538})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.269122838973999})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24382486939430237})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2428652048110962})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2497226744890213})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24422726035118103})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23178060352802277})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22806710004806519})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24512119591236115})
store['active_learning_steps'][87]['eval_training']['best_epoch']=12
store['active_learning_steps'][87]['acquisition']={'indices': [26760, 35624, 34189, 38653, 3816, 50883, 2602, 53215, 25905, 26168], 'labels': [8, -1, -1, -1, -1, -1, -1, -1, -1, 6], 'scores': [0.3955192565917969, 0.5930690765380859, 0.5128191709518433, 0.5698606967926025, 0.487393856048584, 0.41962969303131104, 0.3551269769668579, 0.5706009864807129, 0.5460917949676514, 0.40880805253982544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1844964027404785})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6113187074661255})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40851014852523804})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3281397521495819})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29355037212371826})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2586572766304016})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25675079226493835})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23511332273483276})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2893202304840088})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2714034914970398})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3253348767757416})
store['active_learning_steps'][88]['training']['best_epoch']=8
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.973, 'crossentropy': 0.24047421875}
