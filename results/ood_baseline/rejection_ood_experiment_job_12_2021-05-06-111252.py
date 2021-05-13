store = {}
store['timestamp']=1620295972
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=12']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=40
store['config']={'seed': 15, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.22647762298584})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7895848751068115})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.876115322113037})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.3368749618530273})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6733, 'crossentropy': 2.1569302734375}
store['active_learning_steps'][0]['acquisition']={'indices': [17486, 5017, 34803, 4678, 38256], 'labels': [7, 9, 0, 9, 2], 'scores': [1.185157597064972, 1.1778392791748047, 1.1609311699867249, 1.1484125256538391, 1.143358588218689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.1987648010253906})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.6508662700653076})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9110965728759766})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.46709942817688})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6628, 'crossentropy': 2.03355078125}
store['active_learning_steps'][1]['acquisition']={'indices': [46524, 14749, 48321, 11997, 19609], 'labels': [6, 0, 3, 2, 5], 'scores': [1.1940258741378784, 1.1446672677993774, 1.13241446018219, 1.1159698963165283, 1.1133782267570496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.9381158351898193})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.3423714637756348})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.425574779510498})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.6605513095855713})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6744, 'crossentropy': 1.7243015625}
store['active_learning_steps'][2]['acquisition']={'indices': [42934, 45026, 42540, 15510, 570], 'labels': [2, 8, 8, 2, 2], 'scores': [0.991556704044342, 0.967756450176239, 0.9139149188995361, 0.912704586982727, 0.9072219729423523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.7989182472229004})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.1888694763183594})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.570817470550537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.378807544708252})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6984, 'crossentropy': 1.6748640625}
store['active_learning_steps'][3]['acquisition']={'indices': [21375, 5521, 46329, 12345, 46163], 'labels': [8, 8, 3, 3, 2], 'scores': [1.021596908569336, 1.010539948940277, 1.0082537531852722, 0.9977847933769226, 0.9919925928115845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.7915995121002197})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.279999256134033})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.3887853622436523})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.5734758377075195})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6688, 'crossentropy': 1.706435546875}
store['active_learning_steps'][4]['acquisition']={'indices': [28514, 52708, 39527, 55174, 33830], 'labels': [7, 4, 0, 7, 7], 'scores': [0.8924351930618286, 0.8805545568466187, 0.8762898445129395, 0.8709453344345093, 0.8607633113861084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4619184732437134})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.8624072074890137})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8707926273345947})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.9693843126296997})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7387, 'crossentropy': 1.298901171875}
store['active_learning_steps'][5]['acquisition']={'indices': [22811, 14378, 4797, 20595, 15005], 'labels': [2, 2, 8, 2, 2], 'scores': [0.9715812802314758, 0.9445586800575256, 0.9375461935997009, 0.9350976347923279, 0.9229238033294678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.7289865016937256})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.0269079208374023})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.034147262573242})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.218729257583618})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7022, 'crossentropy': 1.61262578125}
store['active_learning_steps'][6]['acquisition']={'indices': [58249, 9082, 934, 17303, 9769], 'labels': [3, 7, 7, 7, 8], 'scores': [0.8813827037811279, 0.8715851306915283, 0.8587484359741211, 0.8511661887168884, 0.8453185558319092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.4690775871276855})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.9707889556884766})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.0357961654663086})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.3353116512298584})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7294, 'crossentropy': 1.33646982421875}
store['active_learning_steps'][7]['acquisition']={'indices': [26733, 42101, 14121, 37751, 12514], 'labels': [2, 5, 2, 6, 2], 'scores': [0.9176360964775085, 0.870215654373169, 0.8660753965377808, 0.8645148873329163, 0.8462281227111816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.189178228378296})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2884912490844727})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4901647567749023})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.593238115310669})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7949, 'crossentropy': 1.101806640625}
store['active_learning_steps'][8]['acquisition']={'indices': [38512, 14623, 53170, 27083, 54106], 'labels': [5, 5, 8, 7, 7], 'scores': [0.9053558111190796, 0.9000967741012573, 0.8972257375717163, 0.8724628686904907, 0.8685706853866577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.1875659227371216})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4511387348175049})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.4248065948486328})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6767725944519043})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7641, 'crossentropy': 1.10304189453125}
store['active_learning_steps'][9]['acquisition']={'indices': [13030, 13074, 23863, 47619, 29390], 'labels': [0, 0, 9, 0, 9], 'scores': [0.9222638607025146, 0.8800284266471863, 0.8585898876190186, 0.8368954658508301, 0.8201397657394409]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.2321982383728027})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.2996604442596436})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5447275638580322})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.5134892463684082})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7533, 'crossentropy': 1.150691015625}
store['active_learning_steps'][10]['acquisition']={'indices': [20206, 23137, 26286, 32417, 31900], 'labels': [7, 5, 5, 9, 5], 'scores': [0.7964916229248047, 0.7793371677398682, 0.7742776274681091, 0.7686150670051575, 0.765583336353302]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.351204752922058})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4208550453186035})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.7408701181411743})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.6085913181304932})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7226, 'crossentropy': 1.24913017578125}
store['active_learning_steps'][11]['acquisition']={'indices': [34115, 29132, 24501, 43772, 16911], 'labels': [5, 8, 3, 5, 3], 'scores': [0.8922597169876099, 0.7944990396499634, 0.7857843637466431, 0.7829052209854126, 0.7793290615081787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.0887457132339478})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2432670593261719})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.4200289249420166})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.4107860326766968})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.765, 'crossentropy': 1.070424609375}
store['active_learning_steps'][12]['acquisition']={'indices': [27189, 51986, 27503, 47741, 3676], 'labels': [2, 2, 2, 5, 2], 'scores': [0.8141685724258423, 0.7689092755317688, 0.7531010508537292, 0.7268716096878052, 0.7250984907150269]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2370749711990356})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4896808862686157})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.372218132019043})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.637015461921692})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7161, 'crossentropy': 1.1948951171875}
store['active_learning_steps'][13]['acquisition']={'indices': [46476, 15859, 17777, 55864, 27317], 'labels': [5, 7, 3, 3, 5], 'scores': [0.6593127250671387, 0.6248804330825806, 0.6247371435165405, 0.6192090511322021, 0.6186376810073853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.2026005983352661})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1783498525619507})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4972877502441406})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.4869132041931152})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.5515851974487305})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7971, 'crossentropy': 1.118920703125}
store['active_learning_steps'][14]['acquisition']={'indices': [31777, 49890, 19907, 31885, 21356], 'labels': [4, 5, 4, 4, 9], 'scores': [1.0095664262771606, 0.9721383452415466, 0.9565033912658691, 0.9489235877990723, 0.934539258480072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1883609294891357})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2301511764526367})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.3153595924377441})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.496493935585022})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7528, 'crossentropy': 1.173928125}
store['active_learning_steps'][15]['acquisition']={'indices': [3719, 18962, 3791, 22588, 26850], 'labels': [2, 7, 2, 7, 2], 'scores': [0.6984490752220154, 0.6723145246505737, 0.6620075702667236, 0.6592618823051453, 0.6530276536941528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0450572967529297})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0310860872268677})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2230312824249268})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1490716934204102})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1458022594451904})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8415, 'crossentropy': 0.93450166015625}
store['active_learning_steps'][16]['acquisition']={'indices': [19942, 36885, 32572, 22493, 46580], 'labels': [5, 5, 6, 3, 6], 'scores': [0.9817729592323303, 0.9580899477005005, 0.9374933838844299, 0.9352397322654724, 0.9320746064186096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.1387797594070435})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7929789423942566})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8745313882827759})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.871618390083313})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9273834228515625})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8727, 'crossentropy': 0.7507001953125}
store['active_learning_steps'][17]['acquisition']={'indices': [19995, 11708, 1370, 424, 44040], 'labels': [9, 3, 9, 9, 0], 'scores': [0.9530659317970276, 0.9503186345100403, 0.927478551864624, 0.9255767464637756, 0.92341548204422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0222499370574951})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8000808954238892})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8573989868164062})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0161556005477905})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.049898624420166})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8647, 'crossentropy': 0.771040966796875}
store['active_learning_steps'][18]['acquisition']={'indices': [52169, 57985, 44998, 19590, 1364], 'labels': [2, 4, 4, 5, 9], 'scores': [0.8964461088180542, 0.8842436075210571, 0.8816269040107727, 0.8794759511947632, 0.8661023378372192]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.059814214706421})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.88430255651474})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1034648418426514})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.999690055847168})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9610357880592346})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8535, 'crossentropy': 0.810696533203125}
store['active_learning_steps'][19]['acquisition']={'indices': [7033, 10210, 51414, 36744, 16379], 'labels': [7, 3, 8, 1, 7], 'scores': [0.8682401180267334, 0.8668220639228821, 0.864419162273407, 0.8342373371124268, 0.8306752443313599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0597941875457764})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7916338443756104})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8126076459884644})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.133221983909607})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2157092094421387})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8703, 'crossentropy': 0.739760986328125}
store['active_learning_steps'][20]['acquisition']={'indices': [46148, 37974, 3056, 25156, 29472], 'labels': [9, 2, 4, 2, 9], 'scores': [0.850666344165802, 0.8455235362052917, 0.8276135325431824, 0.8274184465408325, 0.8259499073028564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.2666454315185547})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.061353087425232})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0496573448181152})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2011749744415283})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.19956636428833})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.157225489616394})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8448, 'crossentropy': 0.94748056640625}
store['active_learning_steps'][21]['acquisition']={'indices': [46776, 58626, 47132, 58560, 45424], 'labels': [8, 6, 2, 0, 4], 'scores': [0.941344141960144, 0.9317115545272827, 0.9288319945335388, 0.9259842038154602, 0.9230614900588989]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9333734512329102})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7859540581703186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7296478152275085})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8487824201583862})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.972399115562439})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8610939979553223})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8939, 'crossentropy': 0.678999365234375}
store['active_learning_steps'][22]['acquisition']={'indices': [39405, 52697, 36417, 42121, 1674], 'labels': [5, 3, 6, 5, 9], 'scores': [0.986028790473938, 0.9697543978691101, 0.9691199064254761, 0.9685559272766113, 0.9626656174659729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0530109405517578})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8984026908874512})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8507353663444519})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7830288410186768})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8900766372680664})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.085267186164856})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9655171632766724})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8946, 'crossentropy': 0.720757373046875}
store['active_learning_steps'][23]['acquisition']={'indices': [47068, 42384, 28599, 11585, 43782], 'labels': [4, 8, 4, 4, 3], 'scores': [1.0797235369682312, 1.0700048804283142, 1.037282407283783, 1.034375250339508, 0.9940152764320374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.062776803970337})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7429866790771484})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7365957498550415})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7013910412788391})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7458995580673218})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7839468717575073})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8902204036712646})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8978, 'crossentropy': 0.67633955078125}
store['active_learning_steps'][24]['acquisition']={'indices': [8443, 53872, 53873, 20050, 24457], 'labels': [2, 8, 4, 9, 8], 'scores': [1.1927670240402222, 1.0910406708717346, 0.9768697023391724, 0.9598156213760376, 0.9561735987663269]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1142487525939941})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7813738584518433})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.786533772945404})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8800172805786133})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8583863973617554})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8713, 'crossentropy': 0.736029296875}
store['active_learning_steps'][25]['acquisition']={'indices': [50639, 45094, 38974, 22481, 49438], 'labels': [8, 2, 1, 7, 8], 'scores': [0.8263219594955444, 0.8229548335075378, 0.7990273237228394, 0.7983821630477905, 0.7954794764518738]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.060926914215088})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7800542712211609})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6680011749267578})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7366964817047119})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7317773103713989})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7355278730392456})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.6123638671875}
store['active_learning_steps'][26]['acquisition']={'indices': [28512, 3810, 54880, 49536, 9472], 'labels': [5, 3, 5, 5, 2], 'scores': [0.9974430203437805, 0.9754357933998108, 0.9677883386611938, 0.9665399789810181, 0.9591178894042969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0392473936080933})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7107871770858765})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6302376389503479})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7642797231674194})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7819281816482544})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7741256952285767})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.624881884765625}
store['active_learning_steps'][27]['acquisition']={'indices': [1075, 5287, 33812, 41559, 22677], 'labels': [7, 4, 6, 1, 4], 'scores': [0.9567228555679321, 0.9566442966461182, 0.9539226293563843, 0.9318506717681885, 0.9270392656326294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1576226949691772})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7483315467834473})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7081937789916992})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.710476279258728})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8013612031936646})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8445260524749756})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.901, 'crossentropy': 0.663249267578125}
store['active_learning_steps'][28]['acquisition']={'indices': [49149, 57311, 46643, 57369, 57211], 'labels': [3, 5, 4, 5, 5], 'scores': [1.0076330304145813, 1.0065081119537354, 0.9634446501731873, 0.9629336595535278, 0.9555687308311462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.202019453048706})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7032197117805481})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6311806440353394})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6997801065444946})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6841782331466675})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7111826539039612})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9076, 'crossentropy': 0.583068017578125}
store['active_learning_steps'][29]['acquisition']={'indices': [24424, 55128, 20869, 34328, 46368], 'labels': [1, 8, 3, 8, 8], 'scores': [0.880050778388977, 0.8610334992408752, 0.8578932881355286, 0.8526264429092407, 0.84967440366745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9031537175178528})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6773864030838013})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6685006618499756})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6545438766479492})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6965562701225281})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6450678110122681})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7541881799697876})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.728579044342041})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7282779216766357})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9207, 'crossentropy': 0.584197509765625}
store['active_learning_steps'][30]['acquisition']={'indices': [4530, 9180, 36818, 59294, 3146], 'labels': [7, 3, 7, 8, 9], 'scores': [1.0235387682914734, 1.0198904871940613, 1.0040619373321533, 0.9941533803939819, 0.9749454259872437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0329506397247314})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.757906973361969})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6281828880310059})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6948357820510864})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7304182648658752})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7460595965385437})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9139, 'crossentropy': 0.581318408203125}
store['active_learning_steps'][31]['acquisition']={'indices': [31090, 3814, 33505, 53129, 16572], 'labels': [4, 6, 2, 7, 4], 'scores': [0.9847567081451416, 0.919331431388855, 0.8812174201011658, 0.8777984976768494, 0.8724543452262878]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9999622106552124})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6397601366043091})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5992273092269897})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5846121311187744})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5964277982711792})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6456372737884521})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6268603801727295})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.529740576171875}
store['active_learning_steps'][32]['acquisition']={'indices': [42703, 29530, 44661, 17178, 12392], 'labels': [0, 4, 1, 8, 3], 'scores': [0.9436493515968323, 0.9201720952987671, 0.9174906015396118, 0.9116610288619995, 0.9038139581680298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.012121558189392})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6052913665771484})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6264388561248779})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5475270748138428})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5984023213386536})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5799073576927185})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.61390221118927})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9358, 'crossentropy': 0.469165283203125}
store['active_learning_steps'][33]['acquisition']={'indices': [59289, 2367, 54950, 26405, 2427], 'labels': [1, 7, 8, 9, 7], 'scores': [1.0100640058517456, 0.9787946343421936, 0.9769331812858582, 0.9685844779014587, 0.9661586880683899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.009523868560791})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6107051372528076})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.571388304233551})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5244464874267578})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6378161907196045})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.561832070350647})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6516506671905518})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.46220771484375}
store['active_learning_steps'][34]['acquisition']={'indices': [22531, 59783, 16836, 59919, 49525], 'labels': [4, 1, 7, 1, 8], 'scores': [1.0255767703056335, 1.0123769640922546, 0.9884465336799622, 0.9839863777160645, 0.9479492902755737]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1250768899917603})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6211629509925842})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5499210953712463})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5304741859436035})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.590205192565918})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.608087420463562})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6367028951644897})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.50108779296875}
store['active_learning_steps'][35]['acquisition']={'indices': [41999, 33388, 48824, 40953, 12497], 'labels': [0, 8, -1, -1, 0], 'scores': [1.010059654712677, 0.9562241435050964, 0.9546665549278259, 0.9459837079048157, 0.9226571917533875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0766617059707642})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6630600690841675})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6162679195404053})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5675485134124756})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6575136184692383})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6340835094451904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6903666853904724})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.929, 'crossentropy': 0.4913974609375}
store['active_learning_steps'][36]['acquisition']={'indices': [17160, 26444, 30474, 42559, 17958], 'labels': [-1, 1, 6, -1, 9], 'scores': [0.9662230014801025, 0.9638499617576599, 0.9631369113922119, 0.9442092180252075, 0.9282360076904297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1522934436798096})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6162837147712708})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5826994180679321})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5579169392585754})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5641857385635376})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6073521375656128})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6064882278442383})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9366, 'crossentropy': 0.459428662109375}
store['active_learning_steps'][37]['acquisition']={'indices': [42559, 53927, 17160, 57371, 17501], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.9830867648124695, 0.9611133337020874, 0.9595761299133301, 0.9586280584335327, 0.9450168609619141]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.021979570388794})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6240884065628052})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.53565913438797})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5483006834983826})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.530901312828064})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6145318746566772})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5610488653182983})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5999362468719482})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.4541404296875}
store['active_learning_steps'][38]['acquisition']={'indices': [57742, 24462, 20068, 34946, 34847], 'labels': [6, 2, 8, 8, 0], 'scores': [1.0677407383918762, 1.0504741668701172, 0.9886375665664673, 0.9853093028068542, 0.9797304272651672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0302236080169678})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5450051426887512})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49696120619773865})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4854283332824707})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5493177175521851})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5052242279052734})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4845513701438904})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5347057580947876})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5396561026573181})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5597113370895386})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9435, 'crossentropy': 0.4220642578125}
store['active_learning_steps'][39]['acquisition']={'indices': [24479, 5045, 52889, 49039, 46021], 'labels': [8, 9, -1, -1, 9], 'scores': [1.0344290137290955, 1.00299733877182, 0.9808688759803772, 0.9773141145706177, 0.9722990393638611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0150034427642822})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5834277868270874})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5250914692878723})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5206431150436401})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5549795627593994})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5579148530960083})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5363688468933105})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.432750732421875}
store['active_learning_steps'][40]['acquisition']={'indices': [37048, 7833, 36256, 49616, 57972], 'labels': [9, 5, 5, 7, 4], 'scores': [0.9228689074516296, 0.9218090176582336, 0.9178602695465088, 0.9136730432510376, 0.9117223620414734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0299224853515625})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5304169058799744})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4926295280456543})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4509807527065277})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4931405782699585})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5472590327262878})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5139034986495972})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9448, 'crossentropy': 0.399172265625}
store['active_learning_steps'][41]['acquisition']={'indices': [15848, 40752, 32880, 55442, 48681], 'labels': [3, 3, 0, 5, 2], 'scores': [0.9404575824737549, 0.9342725872993469, 0.9048866033554077, 0.8647502064704895, 0.8625434637069702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.062468409538269})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5934359431266785})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5206192135810852})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5546050667762756})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5603023171424866})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5254716873168945})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.46809599609375}
store['active_learning_steps'][42]['acquisition']={'indices': [31301, 1024, 16488, 50371, 31706], 'labels': [5, 5, 9, 7, 8], 'scores': [0.8587429523468018, 0.8580073714256287, 0.843250572681427, 0.8367238640785217, 0.8353701233863831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0476512908935547})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5647804737091064})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.453835666179657})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47496914863586426})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48371389508247375})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46475720405578613})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.4052353515625}
store['active_learning_steps'][43]['acquisition']={'indices': [54885, 13045, 11377, 55743, 11719], 'labels': [6, 3, 3, 3, 3], 'scores': [0.8481194376945496, 0.8326511383056641, 0.8117923736572266, 0.805137038230896, 0.7901058793067932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.294992208480835})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6212832927703857})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5028507113456726})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46536147594451904})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4971003830432892})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4883343577384949})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4695383310317993})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9448, 'crossentropy': 0.4054011474609375}
store['active_learning_steps'][44]['acquisition']={'indices': [20169, 11292, 46975, 42844, 52889], 'labels': [4, 1, -1, 7, -1], 'scores': [0.8719276189804077, 0.841680109500885, 0.8388088941574097, 0.8311940431594849, 0.8196789026260376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0926589965820312})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5585628747940063})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5181684494018555})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4747794568538666})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.44578272104263306})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4520127773284912})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4751376807689667})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.48896825313568115})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9469, 'crossentropy': 0.393392529296875}
store['active_learning_steps'][45]['acquisition']={'indices': [18501, 14896, 42774, 23215, 5155], 'labels': [4, 8, 4, 8, 4], 'scores': [0.9706321358680725, 0.9283782839775085, 0.9187384247779846, 0.8967056274414062, 0.8936923742294312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9325571060180664})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5762218236923218})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45866575837135315})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4076076149940491})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41367805004119873})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48552125692367554})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4869121015071869})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.3950025390625}
store['active_learning_steps'][46]['acquisition']={'indices': [12986, 42428, 33222, 16692, 16210], 'labels': [5, 5, 5, 5, 5], 'scores': [0.9591631293296814, 0.9314090609550476, 0.9012171030044556, 0.8709261417388916, 0.862423300743103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1664445400238037})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5955994725227356})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5012457370758057})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5364205241203308})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4598117172718048})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4678671956062317})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4767634868621826})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.472276508808136})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9389, 'crossentropy': 0.43941552734375}
store['active_learning_steps'][47]['acquisition']={'indices': [52889, 43126, 21910, 28368, 49656], 'labels': [-1, 3, -1, 9, 9], 'scores': [0.9050448536872864, 0.878126859664917, 0.8748518228530884, 0.8640622496604919, 0.863924503326416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1921195983886719})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5866342782974243})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5107021927833557})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46326616406440735})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.47214800119400024})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48755329847335815})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5486709475517273})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9461, 'crossentropy': 0.42033330078125}
store['active_learning_steps'][48]['acquisition']={'indices': [18241, 17121, 34930, 42687, 7270], 'labels': [9, 8, 9, 5, 5], 'scores': [0.9169893264770508, 0.913520336151123, 0.9069818258285522, 0.905678391456604, 0.9024256467819214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0568886995315552})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5510575175285339})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4237947463989258})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4776814579963684})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4602147936820984})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43750327825546265})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9463, 'crossentropy': 0.409680126953125}
store['active_learning_steps'][49]['acquisition']={'indices': [46187, 54994, 42415, 4153, 5842], 'labels': [3, 6, 7, 2, 1], 'scores': [0.7856091856956482, 0.7668193578720093, 0.7591133117675781, 0.7569414973258972, 0.7547234892845154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.228790044784546})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5631659030914307})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5030233263969421})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45896661281585693})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42496395111083984})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4787546992301941})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4360031485557556})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4935927093029022})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.3868587890625}
store['active_learning_steps'][50]['acquisition']={'indices': [4652, 39561, 30177, 52889, 46126], 'labels': [8, 2, 7, -1, 3], 'scores': [0.9278213977813721, 0.8943139314651489, 0.8890184164047241, 0.8786882162094116, 0.8560429215431213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2641010284423828})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6454260349273682})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46892011165618896})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47633880376815796})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4420952796936035})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46202635765075684})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.46622684597969055})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4219076633453369})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4741172194480896})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5023646950721741})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4499533176422119})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.952, 'crossentropy': 0.384018115234375}
store['active_learning_steps'][51]['acquisition']={'indices': [53990, 13021, 32776, 8701, 22139], 'labels': [-1, 5, 4, 8, 2], 'scores': [1.0650396347045898, 1.0355871319770813, 1.0353302955627441, 1.02757066488266, 1.0204320549964905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1272540092468262})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.593635082244873})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4885295629501343})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46768444776535034})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3993889391422272})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4530166685581207})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4683506190776825})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.447997510433197})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.3744186767578125}
store['active_learning_steps'][52]['acquisition']={'indices': [39429, 34739, 20172, 5679, 8104], 'labels': [2, 9, 4, 3, 5], 'scores': [0.9043998122215271, 0.8806654810905457, 0.8791093230247498, 0.872454047203064, 0.8708816766738892]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1293771266937256})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6068528294563293})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49922746419906616})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4863321781158447})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3897598385810852})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43374234437942505})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44694745540618896})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42628633975982666})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.953, 'crossentropy': 0.3389451416015625}
store['active_learning_steps'][53]['acquisition']={'indices': [29376, 18150, 52889, 44028, 16731], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.9731703996658325, 0.9343974590301514, 0.9230014085769653, 0.9107130169868469, 0.9087767601013184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.1892244815826416})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6313201189041138})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46857839822769165})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4087100028991699})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43916282057762146})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4078012704849243})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43454664945602417})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43540287017822266})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4373776614665985})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9523, 'crossentropy': 0.3647621337890625}
store['active_learning_steps'][54]['acquisition']={'indices': [6582, 3012, 11572, 9966, 9340], 'labels': [8, 0, 5, 0, 5], 'scores': [0.8964411020278931, 0.88641357421875, 0.8782012462615967, 0.8723004460334778, 0.8718051910400391]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.121264100074768})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5932604074478149})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5020805597305298})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43776553869247437})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4217148423194885})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41924482583999634})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42947423458099365})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4579693078994751})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4039401710033417})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43849003314971924})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.444233238697052})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4970681965351105})
store['active_learning_steps'][55]['training']['best_epoch']=9
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.3599416015625}
store['active_learning_steps'][55]['acquisition']={'indices': [47626, 18487, 55043, 18398, 38698], 'labels': [-1, 4, -1, 4, 5], 'scores': [1.020909070968628, 1.0186245441436768, 1.0102023482322693, 1.0093053579330444, 1.0042831301689148]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.3242323398590088})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5714629888534546})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4726155400276184})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38605308532714844})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3898692727088928})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4010591506958008})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3883775472640991})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.341237744140625}
store['active_learning_steps'][56]['acquisition']={'indices': [30692, 11028, 5740, 54652, 7949], 'labels': [3, -1, 9, -1, -1], 'scores': [0.8449970483779907, 0.8285019993782043, 0.827054500579834, 0.8268628120422363, 0.8243927955627441]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.3347151279449463})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6665669083595276})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5624115467071533})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45362335443496704})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48516714572906494})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4493679404258728})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5256345272064209})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46734505891799927})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4843599200248718})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9476, 'crossentropy': 0.40710302734375}
store['active_learning_steps'][57]['acquisition']={'indices': [42787, 57053, 6832, 36072, 20171], 'labels': [4, 0, 0, 2, 5], 'scores': [0.9655851721763611, 0.9555890560150146, 0.9495329856872559, 0.9485565423965454, 0.9482167959213257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.4216854572296143})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6909598112106323})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.502156138420105})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4439833462238312})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4681466519832611})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4597540497779846})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.44133538007736206})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.48957639932632446})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4236179292201996})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40177807211875916})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.49499693512916565})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.451798677444458})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4353470206260681})
store['active_learning_steps'][58]['training']['best_epoch']=10
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.362391259765625}
store['active_learning_steps'][58]['acquisition']={'indices': [23956, 53990, 4379, 32499, 391], 'labels': [4, -1, -1, 4, 2], 'scores': [1.0879754424095154, 1.0478523969650269, 1.046368420124054, 1.0121659636497498, 1.0084291100502014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2091395854949951})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6538499593734741})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4840708374977112})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39455607533454895})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35592567920684814})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44943851232528687})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4411427974700928})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45047032833099365})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.3231355224609375}
store['active_learning_steps'][59]['acquisition']={'indices': [18324, 57718, 30658, 14305, 52889], 'labels': [0, 7, 4, 8, -1], 'scores': [0.9395240545272827, 0.895588219165802, 0.8898490071296692, 0.8887531757354736, 0.8874946236610413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.3753108978271484})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6445424556732178})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5446041822433472})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4769342541694641})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5324720740318298})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.49803486466407776})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4686815142631531})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5267817974090576})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4665380120277405})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5013911128044128})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5454165935516357})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.54045569896698})
store['active_learning_steps'][60]['training']['best_epoch']=9
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.4051083251953125}
store['active_learning_steps'][60]['acquisition']={'indices': [49282, 25384, 1518, 43702, 57956], 'labels': [2, 5, 9, 3, 2], 'scores': [1.0817071497440338, 1.0671623349189758, 1.0669971704483032, 1.0291976928710938, 1.023247480392456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.3631088733673096})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6742045283317566})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5363740921020508})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4525517523288727})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42847999930381775})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44151780009269714})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3981163501739502})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4300289750099182})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4623996317386627})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4548794627189636})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.339808154296875}
store['active_learning_steps'][61]['acquisition']={'indices': [47626, 470, 51736, 37016, 37469], 'labels': [-1, 1, 5, 5, 2], 'scores': [1.0760071277618408, 1.04911607503891, 1.04004967212677, 1.027772307395935, 1.017640769481659]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3877661228179932})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6623936891555786})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45826804637908936})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4224746823310852})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4126942753791809})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42065975069999695})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43688535690307617})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40779316425323486})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4243851900100708})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4514898657798767})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.47256386280059814})
store['active_learning_steps'][62]['training']['best_epoch']=8
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.318459228515625}
store['active_learning_steps'][62]['acquisition']={'indices': [28357, 15932, 43648, 49563, 41933], 'labels': [0, 7, 5, 8, 5], 'scores': [1.0509527325630188, 1.0383517146110535, 1.0356572270393372, 1.023480474948883, 1.0213008522987366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4241225719451904})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6971523761749268})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5046712160110474})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4414394497871399})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42247337102890015})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41693899035453796})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40613994002342224})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.44388851523399353})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4228641390800476})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4571499526500702})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.3658768310546875}
store['active_learning_steps'][63]['acquisition']={'indices': [11767, 8297, 32173, 3136, 32926], 'labels': [4, 7, 7, 6, 8], 'scores': [0.9914878010749817, 0.9801666736602783, 0.9552947282791138, 0.9479862451553345, 0.9433192610740662]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4072763919830322})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7230663299560547})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4930906295776367})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4618685245513916})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45279085636138916})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4453360438346863})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40736693143844604})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42281192541122437})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45885491371154785})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43125486373901367})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9575, 'crossentropy': 0.354960791015625}
store['active_learning_steps'][64]['acquisition']={'indices': [17540, 55906, 8879, 16011, 56014], 'labels': [1, 2, 3, 5, 5], 'scores': [0.9976034164428711, 0.9889779090881348, 0.9599161744117737, 0.9588278532028198, 0.9476405382156372]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.3660670518875122})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6488641500473022})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.524016261100769})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4714696407318115})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4438724219799042})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43031615018844604})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4480511546134949})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4399377107620239})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4453238844871521})
store['active_learning_steps'][65]['training']['best_epoch']=6
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9511, 'crossentropy': 0.386305810546875}
store['active_learning_steps'][65]['acquisition']={'indices': [45602, 47626, 20641, 12305, 36450], 'labels': [5, -1, 9, 9, 2], 'scores': [0.9943863749504089, 0.9748597741127014, 0.9208459258079529, 0.9040128588676453, 0.9025530219078064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.2834818363189697})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.65534907579422})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4787485599517822})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4578879773616791})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4986181855201721})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45608070492744446})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.49022746086120605})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44503235816955566})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.46096083521842957})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4519391655921936})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4468662440776825})
store['active_learning_steps'][66]['training']['best_epoch']=8
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9555, 'crossentropy': 0.38715849609375}
store['active_learning_steps'][66]['acquisition']={'indices': [50946, 966, 20057, 53507, 13998], 'labels': [3, 3, 6, 5, 9], 'scores': [1.02652245759964, 1.0227416157722473, 0.9459342658519745, 0.9250249564647675, 0.9153516888618469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2735788822174072})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6711108088493347})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5140507221221924})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4356633126735687})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40124785900115967})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3858933448791504})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39253222942352295})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4618067741394043})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41903233528137207})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.3383967529296875}
store['active_learning_steps'][67]['acquisition']={'indices': [2845, 42559, 6604, 42199, 7168], 'labels': [8, -1, 8, 3, 8], 'scores': [0.9081421494483948, 0.876131534576416, 0.8653163909912109, 0.8651384115219116, 0.8607348203659058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.4543827772140503})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7802777290344238})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5776752233505249})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4806094467639923})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4179849624633789})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4233753979206085})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44218459725379944})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47337907552719116})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.368146875}
store['active_learning_steps'][68]['acquisition']={'indices': [4955, 48006, 50403, 5013, 28930], 'labels': [2, 6, -1, 2, 7], 'scores': [0.9590951800346375, 0.9121389985084534, 0.8913486003875732, 0.8903748393058777, 0.8878629803657532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2268214225769043})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6727772951126099})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.464674174785614})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38368767499923706})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4256659150123596})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3957381248474121})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3768227994441986})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3738534450531006})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43277275562286377})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4712744355201721})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45015949010849})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3281492919921875}
store['active_learning_steps'][69]['acquisition']={'indices': [25294, 21952, 13942, 15771, 50403], 'labels': [2, 2, 4, 5, -1], 'scores': [0.9828077554702759, 0.975969135761261, 0.9489291608333588, 0.9206925630569458, 0.9143298864364624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.378240942955017})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6868728399276733})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5130555629730225})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.424094557762146})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4046475887298584})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3606370687484741})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42191100120544434})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4055730700492859})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3898347020149231})
store['active_learning_steps'][70]['training']['best_epoch']=6
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.316226123046875}
store['active_learning_steps'][70]['acquisition']={'indices': [53990, 45171, 55778, 43045, 30851], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.9104804396629333, 0.8878428936004639, 0.8615692853927612, 0.850908100605011, 0.8477078080177307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4222569465637207})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7153217196464539})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.48759832978248596})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41425561904907227})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40293359756469727})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37712132930755615})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38822367787361145})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40146756172180176})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36680829524993896})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4371688961982727})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4198954105377197})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.44313862919807434})
store['active_learning_steps'][71]['training']['best_epoch']=9
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.32569228515625}
store['active_learning_steps'][71]['acquisition']={'indices': [37094, 59747, 25873, 25879, 31], 'labels': [8, 5, 8, 8, 8], 'scores': [1.031411051750183, 1.0275306105613708, 1.0065297484397888, 0.9896947145462036, 0.9859089851379395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4475631713867188})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.7228974103927612})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5108625888824463})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.45685356855392456})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39729297161102295})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4466535449028015})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4003336429595947})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39872124791145325})
store['active_learning_steps'][72]['training']['best_epoch']=5
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9596, 'crossentropy': 0.3500529052734375}
store['active_learning_steps'][72]['acquisition']={'indices': [48102, 52661, 635, 30883, 10256], 'labels': [7, 3, 5, 3, 2], 'scores': [0.8629998564720154, 0.859404444694519, 0.8486274480819702, 0.8480122685432434, 0.8445584177970886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.4741954803466797})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6795697808265686})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5507104396820068})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41848957538604736})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37623798847198486})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35719621181488037})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36834487318992615})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3466757535934448})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34217554330825806})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3337869942188263})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3834487199783325})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4312807321548462})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38138526678085327})
store['active_learning_steps'][73]['training']['best_epoch']=10
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.3210048828125}
store['active_learning_steps'][73]['acquisition']={'indices': [42028, 31738, 25036, 12430, 4248], 'labels': [1, 8, 1, -1, 1], 'scores': [1.0758274793624878, 1.0695213079452515, 1.0536341667175293, 1.0296815037727356, 1.0151289701461792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.3192040920257568})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.6404508352279663})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44152817130088806})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.43083125352859497})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3927217721939087})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38936254382133484})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.39038145542144775})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3497169613838196})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.408122718334198})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.358355313539505})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38696181774139404})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.3127954833984375}
store['active_learning_steps'][74]['acquisition']={'indices': [22083, 29018, 41007, 38912, 52889], 'labels': [2, -1, -1, -1, -1], 'scores': [0.9927979707717896, 0.964568018913269, 0.9630360007286072, 0.9598691463470459, 0.9259456396102905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.3052759170532227})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6916055679321289})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.509009063243866})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4311707615852356})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41543489694595337})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4413875639438629})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4212104082107544})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3900516927242279})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4005318284034729})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36570364236831665})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3859022855758667})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3817041516304016})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3978545665740967})
store['active_learning_steps'][75]['training']['best_epoch']=10
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.3192242919921875}
store['active_learning_steps'][75]['acquisition']={'indices': [5065, 50840, 10520, 19663, 31557], 'labels': [2, 2, -1, -1, -1], 'scores': [1.0717670917510986, 0.9806123673915863, 0.9743754863739014, 0.9707150459289551, 0.9658783674240112]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3433349132537842})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6728142499923706})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4896673858165741})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4448314607143402})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3873421549797058})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40123385190963745})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3911096453666687})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4219011962413788})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9581, 'crossentropy': 0.357487060546875}
store['active_learning_steps'][76]['acquisition']={'indices': [42020, 41924, 49354, 45800, 6050], 'labels': [9, 9, 0, 9, 7], 'scores': [0.8771525621414185, 0.8735427260398865, 0.8447167277336121, 0.8441593647003174, 0.8228607475757599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3848998546600342})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6993651390075684})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.49622052907943726})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4688684940338135})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3746671974658966})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3460167646408081})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.409594863653183})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4172186255455017})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.383322149515152})
store['active_learning_steps'][77]['training']['best_epoch']=6
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.3208587646484375}
store['active_learning_steps'][77]['acquisition']={'indices': [9608, 36508, 1682, 1239, 18255], 'labels': [8, 5, 0, 8, -1], 'scores': [1.018529236316681, 0.9069257974624634, 0.9022972583770752, 0.8925451636314392, 0.8795600533485413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.398899793624878})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6990895867347717})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5144963264465332})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46436458826065063})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3996199369430542})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3517761826515198})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4190570116043091})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3790057301521301})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4289802312850952})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9603, 'crossentropy': 0.3326765380859375}
store['active_learning_steps'][78]['acquisition']={'indices': [47626, 52889, 53990, 11534, 4379], 'labels': [-1, -1, -1, 7, -1], 'scores': [0.9608609676361084, 0.9445717930793762, 0.9165439009666443, 0.915595293045044, 0.8917573690414429]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.261788010597229})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7542012929916382})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5100687146186829})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4345284104347229})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4061925411224365})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4049363136291504})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39717942476272583})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3755551278591156})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44746270775794983})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3951745331287384})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3909691572189331})
store['active_learning_steps'][79]['training']['best_epoch']=8
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.31518779296875}
store['active_learning_steps'][79]['acquisition']={'indices': [56190, 45446, 19868, 250, 32878], 'labels': [4, 7, 5, 3, 9], 'scores': [0.9830137491226196, 0.9787082672119141, 0.9505444169044495, 0.9397809505462646, 0.9380858540534973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.4574594497680664})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7210050821304321})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5338776707649231})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40900641679763794})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38973480463027954})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4632760286331177})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3462572693824768})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.41301584243774414})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38091206550598145})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40669363737106323})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3354835693359375}
store['active_learning_steps'][80]['acquisition']={'indices': [20186, 31474, 27964, 3980, 21896], 'labels': [5, 8, 8, 2, 8], 'scores': [0.9057318568229675, 0.8906848430633545, 0.8880317807197571, 0.8730289340019226, 0.8705006241798401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.4410921335220337})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7231369018554688})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.486380934715271})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45466533303260803})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38317257165908813})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3766564726829529})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32633504271507263})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3670322895050049})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37715470790863037})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35211268067359924})
store['active_learning_steps'][81]['training']['best_epoch']=7
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.319888720703125}
store['active_learning_steps'][81]['acquisition']={'indices': [21211, 23971, 29376, 35401, 52889], 'labels': [-1, 0, -1, 3, -1], 'scores': [0.9335123300552368, 0.9086675643920898, 0.8968704342842102, 0.8945780396461487, 0.892501711845398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.4277899265289307})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7298407554626465})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.528484046459198})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4259841740131378})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4348805546760559})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43276527523994446})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3882169723510742})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.40002351999282837})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35544395446777344})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45170971751213074})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3729473352432251})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3789857029914856})
store['active_learning_steps'][82]['training']['best_epoch']=9
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.331087646484375}
store['active_learning_steps'][82]['acquisition']={'indices': [40654, 53694, 53844, 54035, 38912], 'labels': [5, 7, 5, 7, -1], 'scores': [1.0261306166648865, 0.9525708556175232, 0.9447416067123413, 0.9342018961906433, 0.9313963651657104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.3737916946411133})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7482030391693115})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49684202671051025})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4153740406036377})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3939122259616852})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3569016456604004})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4124182462692261})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3739306330680847})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3808886408805847})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.33832822265625}
store['active_learning_steps'][83]['acquisition']={'indices': [32355, 42904, 18682, 15988, 1512], 'labels': [8, 6, 7, 8, 0], 'scores': [0.8187251091003418, 0.7954986691474915, 0.7944028973579407, 0.7904333472251892, 0.790305495262146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4108092784881592})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.698102593421936})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4968496263027191})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41482818126678467})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.35596010088920593})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39274731278419495})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3589995503425598})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37144365906715393})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.3167704345703125}
store['active_learning_steps'][84]['acquisition']={'indices': [8670, 6309, 7192, 59081, 50572], 'labels': [2, 3, 3, -1, 1], 'scores': [0.8626446723937988, 0.830734372138977, 0.8252883553504944, 0.8221340179443359, 0.8148778676986694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2871628999710083})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5967063903808594})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.44223877787590027})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36712706089019775})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33726051449775696})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39441776275634766})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32128405570983887})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33750197291374207})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.344798743724823})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32960399985313416})
store['active_learning_steps'][85]['training']['best_epoch']=7
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.30083486328125}
store['active_learning_steps'][85]['acquisition']={'indices': [35482, 26568, 31252, 19159, 20037], 'labels': [4, -1, 5, 8, 8], 'scores': [0.9313832521438599, 0.9293911457061768, 0.9149047136306763, 0.9085520505905151, 0.8830609917640686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.4216136932373047})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8093811273574829})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4747380316257477})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41292518377304077})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.42529910802841187})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3901170492172241})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3973454236984253})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3610425889492035})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3822106122970581})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3343343436717987})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3931691646575928})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.379753053188324})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.403270959854126})
store['active_learning_steps'][86]['training']['best_epoch']=10
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.314063818359375}
store['active_learning_steps'][86]['acquisition']={'indices': [45069, 50459, 17019, 38912, 9147], 'labels': [4, 8, 9, -1, 4], 'scores': [0.9620832204818726, 0.9236109852790833, 0.91166752576828, 0.9047064185142517, 0.8913764357566833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.4510592222213745})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8147857189178467})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.5007371306419373})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.45212501287460327})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3639066517353058})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.340915322303772})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3821571469306946})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32276487350463867})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3517214059829712})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37201017141342163})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.35266128182411194})
store['active_learning_steps'][87]['training']['best_epoch']=8
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.3126314697265625}
store['active_learning_steps'][87]['acquisition']={'indices': [59314, 29711, 47209, 46899, 22607], 'labels': [9, 8, 6, 3, 4], 'scores': [0.8977962136268616, 0.8898149728775024, 0.8737704157829285, 0.8697882294654846, 0.8690527081489563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.329965591430664})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6649035215377808})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4600585103034973})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3803355097770691})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36895036697387695})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.36229056119918823})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3531092405319214})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3395445942878723})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.34585705399513245})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35618138313293457})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3543272614479065})
store['active_learning_steps'][88]['training']['best_epoch']=8
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.3110802001953125}
store['active_learning_steps'][88]['acquisition']={'indices': [47626, 15738, 40398, 34665, 26882], 'labels': [-1, -1, -1, 9, 7], 'scores': [1.0469447374343872, 1.00593763589859, 0.9701980352401733, 0.9591545462608337, 0.9450997114181519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.4545594453811646})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7837581634521484})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.49282002449035645})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4591410756111145})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37195441126823425})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36700087785720825})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3814159333705902})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33409905433654785})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3488886058330536})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.34915781021118164})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35571831464767456})
store['active_learning_steps'][89]['training']['best_epoch']=8
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.303954833984375}
store['active_learning_steps'][89]['acquisition']={'indices': [54570, 8447, 33162, 59081, 36196], 'labels': [6, 3, 8, -1, -1], 'scores': [0.9184360802173615, 0.9175547361373901, 0.91592937707901, 0.9139817953109741, 0.9079523682594299]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.5276284217834473})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.781052827835083})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.49504438042640686})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41536974906921387})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3598991632461548})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3403337597846985})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3410925269126892})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31631046533584595})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.31006163358688354})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.34955546259880066})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3468922972679138})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34568870067596436})
store['active_learning_steps'][90]['training']['best_epoch']=9
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.297480419921875}
store['active_learning_steps'][90]['acquisition']={'indices': [9552, 15781, 20792, 13946, 26538], 'labels': [0, 5, 9, 5, 5], 'scores': [1.0148667693138123, 0.952344536781311, 0.9487181305885315, 0.9194680452346802, 0.9003832340240479]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.555272102355957})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7966179847717285})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5547200441360474})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.4528888165950775})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3787357807159424})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3721311092376709})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.33719396591186523})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3639482259750366})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3701646327972412})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3245304226875305})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36604443192481995})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.38159769773483276})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3789476156234741})
store['active_learning_steps'][91]['training']['best_epoch']=10
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.303397021484375}
store['active_learning_steps'][91]['acquisition']={'indices': [52889, 49573, 5315, 45171, 47034], 'labels': [-1, 2, 3, -1, -1], 'scores': [1.0401228666305542, 1.0203064680099487, 0.9982985258102417, 0.986009418964386, 0.9757393598556519]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 1.5592594146728516})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8202166557312012})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5128620862960815})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.43690454959869385})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3696134388446808})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35291212797164917})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34896326065063477})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3833271861076355})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3422277867794037})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.39712560176849365})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3728561997413635})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4560354948043823})
store['active_learning_steps'][92]['training']['best_epoch']=9
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.3098827392578125}
store['active_learning_steps'][92]['acquisition']={'indices': [14210, 58445, 59406, 39411, 38912], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.0180104970932007, 1.0100314617156982, 0.9847034215927124, 0.9719464182853699, 0.9627548456192017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.491045594215393})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.7425674200057983})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5189505219459534})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4454701542854309})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40448206663131714})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3857543468475342})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.37079888582229614})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35842230916023254})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37774431705474854})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.36564600467681885})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39071857929229736})
store['active_learning_steps'][93]['training']['best_epoch']=8
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.33132880859375}
store['active_learning_steps'][93]['acquisition']={'indices': [37583, 43950, 54401, 36409, 57728], 'labels': [-1, 9, -1, 3, 9], 'scores': [0.9448152780532837, 0.9324497580528259, 0.9315444231033325, 0.9217388033866882, 0.9188199043273926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.4842848777770996})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6679562330245972})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.5154843330383301})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3895658254623413})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38388702273368835})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.398404061794281})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33025476336479187})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3533326983451843})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3778223991394043})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36248070001602173})
store['active_learning_steps'][94]['training']['best_epoch']=7
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.32105224609375}
store['active_learning_steps'][94]['acquisition']={'indices': [5000, 31958, 47220, 59081, 50370], 'labels': [7, -1, 6, -1, 7], 'scores': [0.9214107692241669, 0.8966809511184692, 0.892742931842804, 0.8864989280700684, 0.8758728504180908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5617481470108032})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.772513210773468})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.5004978775978088})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.393892765045166})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3823792338371277})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37648582458496094})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3401593267917633})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33725854754447937})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3814469873905182})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34885135293006897})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3308577537536621})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3556404113769531})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3446977734565735})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3456195592880249})
store['active_learning_steps'][95]['training']['best_epoch']=11
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.3089168212890625}
store['active_learning_steps'][95]['acquisition']={'indices': [22163, 28392, 52889, 41453, 20036], 'labels': [-1, 3, -1, 3, 1], 'scores': [1.0460026264190674, 1.044839859008789, 0.9578365087509155, 0.9499281644821167, 0.9481217861175537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.6130518913269043})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.866258442401886})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5537655353546143})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4933245778083801})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33835163712501526})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40969106554985046})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4139068126678467})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3568916916847229})
store['active_learning_steps'][96]['training']['best_epoch']=5
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.343572607421875}
store['active_learning_steps'][96]['acquisition']={'indices': [36704, 41802, 21174, 14201, 34396], 'labels': [2, 2, 2, 7, 3], 'scores': [0.8091070055961609, 0.7846283316612244, 0.7798786163330078, 0.7754001021385193, 0.7702735066413879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 1.4526727199554443})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7758044004440308})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5563445687294006})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3574954867362976})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37256920337677})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3152638375759125})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3617151081562042})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3442917466163635})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3587765395641327})
store['active_learning_steps'][97]['training']['best_epoch']=6
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.3107009033203125}
store['active_learning_steps'][97]['acquisition']={'indices': [53990, 50736, 37078, 58472, 4564], 'labels': [-1, -1, 8, 2, -1], 'scores': [0.9580879211425781, 0.912578821182251, 0.9036279320716858, 0.8864758014678955, 0.8836729526519775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.473845362663269})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7201783061027527})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.508853018283844})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4279164671897888})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4013879597187042})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3261794149875641})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35434937477111816})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3511848747730255})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3310064673423767})
store['active_learning_steps'][98]['training']['best_epoch']=6
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.3136165771484375}
store['active_learning_steps'][98]['acquisition']={'indices': [36268, 32342, 52889, 15738, 29376], 'labels': [5, 9, -1, -1, -1], 'scores': [0.8274560570716858, 0.8061892986297607, 0.8058061599731445, 0.8056460618972778, 0.7949919700622559]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.5634765625, 'crossentropy': 1.5296728610992432})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6565783023834229})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4601696729660034})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41005533933639526})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41491371393203735})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35826727747917175})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3425508141517639})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3515987992286682})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34166136384010315})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37360817193984985})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.388097882270813})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3602476119995117})
store['active_learning_steps'][99]['training']['best_epoch']=9
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.3023648681640625}
store['active_learning_steps'][99]['acquisition']={'indices': [48824, 44364, 21674, 18983, 41228], 'labels': [-1, 2, 2, -1, 0], 'scores': [0.9397854804992676, 0.9388459920883179, 0.9237657785415649, 0.9208905100822449, 0.9160605370998383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.634185552597046})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8245490789413452})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5347469449043274})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39350321888923645})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.39770278334617615})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32947593927383423})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33575522899627686})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3785730302333832})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33245086669921875})
store['active_learning_steps'][100]['training']['best_epoch']=6
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.317495849609375}
store['active_learning_steps'][100]['acquisition']={'indices': [2148, 19344, 29376, 57507, 30493], 'labels': [6, 7, -1, 0, 1], 'scores': [0.872730553150177, 0.82184898853302, 0.8179489374160767, 0.8174158930778503, 0.8129768371582031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5228502750396729})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.8007432222366333})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5198315382003784})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.43527716398239136})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3980811834335327})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35032790899276733})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3876352310180664})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36174917221069336})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3576951026916504})
store['active_learning_steps'][101]['training']['best_epoch']=6
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.3197419189453125}
store['active_learning_steps'][101]['acquisition']={'indices': [52889, 43575, 34520, 59081, 54652], 'labels': [-1, 2, 6, -1, -1], 'scores': [0.9177404642105103, 0.8575635552406311, 0.833830714225769, 0.8326906561851501, 0.8222010731697083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.5230677127838135})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7677643299102783})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.47985246777534485})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3719976544380188})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3478394150733948})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3353397846221924})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3217398524284363})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35676485300064087})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3196982145309448})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33996397256851196})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30944809317588806})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36358553171157837})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3439942002296448})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3643072247505188})
store['active_learning_steps'][102]['training']['best_epoch']=11
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2764958984375}
store['active_learning_steps'][102]['acquisition']={'indices': [13969, 4850, 53990, 47626, 29376], 'labels': [3, 3, -1, -1, -1], 'scores': [0.9740555286407471, 0.9599632024765015, 0.9504942893981934, 0.9397410750389099, 0.9281139969825745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.3683425188064575})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7683488130569458})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.45367714762687683})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.401949942111969})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3391331434249878})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3311381936073303})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3523498475551605})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3087773323059082})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2800372838973999})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3200937807559967})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32623475790023804})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3317510783672333})
store['active_learning_steps'][103]['training']['best_epoch']=9
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2652591796875}
store['active_learning_steps'][103]['acquisition']={'indices': [32583, 50916, 10520, 52889, 44570], 'labels': [-1, 4, -1, -1, 7], 'scores': [0.9817988872528076, 0.9426063299179077, 0.928494930267334, 0.9041820764541626, 0.9011595249176025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.5673612356185913})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7635162472724915})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5183972120285034})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40337294340133667})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37901100516319275})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34455758333206177})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3359602689743042})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33105364441871643})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.351889431476593})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3340941071510315})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38015055656433105})
store['active_learning_steps'][104]['training']['best_epoch']=8
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.2831803466796875}
store['active_learning_steps'][104]['acquisition']={'indices': [27429, 53990, 52889, 13259, 43112], 'labels': [0, -1, -1, 1, -1], 'scores': [1.0058600902557373, 0.9671508073806763, 0.9396533966064453, 0.9314041137695312, 0.9008049964904785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.5810546875, 'crossentropy': 1.5526819229125977})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.765995442867279})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5079227685928345})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41730576753616333})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4005146622657776})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33263543248176575})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.377136766910553})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3476410508155823})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32666561007499695})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3319375216960907})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3145623803138733})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34422147274017334})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36424165964126587})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.36425191164016724})
store['active_learning_steps'][105]['training']['best_epoch']=11
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2966284423828125}
store['active_learning_steps'][105]['acquisition']={'indices': [52889, 20859, 52086, 49910, 29672], 'labels': [-1, 8, 5, 6, 9], 'scores': [1.0530421733856201, 0.9700267314910889, 0.9405743479728699, 0.9359750747680664, 0.9242062568664551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2596896886825562})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6811103224754333})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.49615415930747986})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.42522138357162476})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36997005343437195})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.35661518573760986})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37016773223876953})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3621551990509033})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34565556049346924})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33396416902542114})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3760034441947937})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33866432309150696})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34310805797576904})
store['active_learning_steps'][106]['training']['best_epoch']=10
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.3128896728515625}
