store = {}
store['timestamp']=1622064925
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=6']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=80
store['config']={'seed': 1240, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('FastFashionMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.504277229309082})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3698782920837402})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.887885570526123})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.925203800201416})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6962, 'crossentropy': 2.0238193359375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2409907579421997})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1650012731552124})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1619441509246826})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 35151], ['id', 36475], ['id', 59440], ['id', 9687], ['id', 5499]], 'labels': [5, 2, 3, 0, 5], 'scores': [1.0479821976096426, 1.8148679239724799, 2.378100481775183, 2.800900017713138, 3.0647796005127734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.5498812198638916})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 2.9699106216430664})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9975333213806152})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.547726631164551})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.4395952224731445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 3.5228796005249023})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6649, 'crossentropy': 2.68750390625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.306032419204712})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.271735429763794})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.296850562095642})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.2742013931274414})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.2773025035858154})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 47765], ['id', 3782], ['id', 10307], ['id', 12379], ['ood', 10082]], 'labels': [8, 7, 6, 8, -1], 'scores': [1.11813333819131, 2.017244711929717, 2.6226653483685514, 2.9902468198833354, 3.1702358979298273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.9459331035614014})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.492741107940674})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7267355918884277})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.0173254013061523})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6963, 'crossentropy': 1.8239033203125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0578179359436035})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0764508247375488})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.0075623989105225})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 25521], ['id', 44013], ['id', 32348], ['id', 12595], ['id', 42805]], 'labels': [5, 4, 5, 4, 2], 'scores': [0.927088935159204, 1.7144122095475485, 2.296309094451738, 2.7306312098058942, 2.998532192253598]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.5728225708007812})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.7368857860565186})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.063230514526367})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.9904885292053223})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8086163997650146})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.053095817565918})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 2.277186870574951})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.5158286094665527})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.788, 'crossentropy': 1.53883896484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9697680473327637})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8763232231140137})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8802495002746582})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.8652793169021606})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.8195191621780396})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.849112868309021})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.8115105032920837})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 29132], ['id', 57311], ['id', 42709], ['id', 5155], ['id', 48384]], 'labels': [8, 5, 9, 4, 9], 'scores': [0.996535012796778, 1.875238139009284, 2.524447151477644, 2.901899771431573, 3.098085836516291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.8237900733947754})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.0809123516082764})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.1914429664611816})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 2.2211601734161377})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.42830491065979})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.429842710494995})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.4675636291503906})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7558, 'crossentropy': 1.91152890625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0816359519958496})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0183161497116089})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9971320629119873})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9888705015182495})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9510712623596191})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9433003664016724})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 21399], ['id', 53170], ['id', 47214], ['id', 19005], ['id', 24748]], 'labels': [8, 8, 6, 8, 3], 'scores': [0.9754328104471053, 1.7470275200767498, 2.3240019741519182, 2.724539312572963, 2.957617561444401]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.4354063272476196})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.6487476825714111})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.9106104373931885})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.019763231277466})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.131937265396118})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7828, 'crossentropy': 1.4615564453125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.909020185470581})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.8587877750396729})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8344794511795044})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.8490598201751709})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 37397], ['id', 42428], ['id', 4066], ['id', 4058], ['id', 48789]], 'labels': [3, 5, 1, 8, 9], 'scores': [0.9141259937481121, 1.693238366744283, 2.2919006017537544, 2.6825634028610015, 2.912324147398964]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.478363037109375})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.8113317489624023})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.8328903913497925})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.2140932083129883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.207825183868408})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 2.362717628479004})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 2.0404884815216064})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 2.120586395263672})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 2.269594192504883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.41037654876709})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 2.3373701572418213})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.680511713027954})
store['active_learning_steps'][6]['training']['best_epoch']=9
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7861, 'crossentropy': 2.075834375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0220592021942139})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.9121611714363098})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8933393955230713})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.861517071723938})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8571906089782715})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8768938779830933})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.853746771812439})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 29453], ['id', 2835], ['id', 48281], ['id', 49491], ['id', 33622]], 'labels': [2, 7, 3, 7, 5], 'scores': [1.0406469144915467, 1.9315102534527764, 2.6141022756644556, 2.9391970516860884, 3.0587470172411395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.2979639768600464})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6531281471252441})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.834582805633545})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.0805506706237793})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.792521595954895})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 2.340519905090332})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.8857759237289429})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.454960823059082})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 2.2825398445129395})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 2.152926206588745})
store['active_learning_steps'][7]['training']['best_epoch']=7
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7979, 'crossentropy': 1.722848046875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0144367218017578})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8315838575363159})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8858652114868164})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8487107753753662})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8269704580307007})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 15855], ['id', 42237], ['id', 7262], ['id', 45230], ['ood', 27998]], 'labels': [5, 5, 2, 0, -1], 'scores': [0.9253210088005464, 1.678630798555532, 2.244046689550168, 2.609278559074876, 2.800792393159048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2151439189910889})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.361130952835083})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4721204042434692})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5299079418182373})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.6192342042922974})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.5923559665679932})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.7263553142547607})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.8738378286361694})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.7409037351608276})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8394, 'crossentropy': 1.4495541015625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8170005083084106})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8222755193710327})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.738861083984375})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7650699615478516})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7136107683181763})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.7663575410842896})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 34085], ['id', 20869], ['id', 207], ['id', 2732], ['id', 59847]], 'labels': [3, 3, 3, 4, 0], 'scores': [0.8964455310112196, 1.6786258399529892, 2.260512575880865, 2.627001557731864, 2.8464610749985706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1412094831466675})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.335581660270691})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3734302520751953})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3089669942855835})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6786658763885498})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.5279974937438965})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.4804301261901855})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8426, 'crossentropy': 1.2222947265625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8540691137313843})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7922638654708862})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.773106038570404})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7368459701538086})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7133762240409851})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7390078902244568})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 23385], ['id', 49895], ['id', 39474], ['id', 56300], ['id', 43234]], 'labels': [5, 5, 0, 9, 8], 'scores': [0.8775420465694181, 1.5874461212284472, 2.136737102610809, 2.503648467988211, 2.7069838109897972]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2573070526123047})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.501951813697815})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5861217975616455})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.6253349781036377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.6342201232910156})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.7337850332260132})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.9149253368377686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 2.1202688217163086})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8465, 'crossentropy': 1.41850859375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8753083944320679})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8212106227874756})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.7887333035469055})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7713343501091003})
store['active_learning_steps'][10]['eval_training']['best_epoch']=1
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 27793], ['id', 3494], ['id', 9098], ['id', 50584], ['id', 13496]], 'labels': [1, 7, 2, 6, 3], 'scores': [0.8119922390367234, 1.516548051911693, 2.0233538882509183, 2.3531665527361296, 2.5459795276710775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.101226568222046})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.079969048500061})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2510883808135986})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.259598970413208})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4421310424804688})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.614745855331421})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.7105283737182617})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8599, 'crossentropy': 1.06988134765625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8408782482147217})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7230573892593384})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6636325120925903})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6297239065170288})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6255596876144409})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.637719452381134})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 1549], ['id', 13259], ['id', 14072], ['id', 45373], ['id', 55053]], 'labels': [2, 1, 6, 1, 4], 'scores': [0.9102955432362019, 1.7089569380473417, 2.353915997135749, 2.74763673987286, 2.9558714543231055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9363752603530884})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9343773126602173})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.963354229927063})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9966331720352173})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0756957530975342})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0642613172531128})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0620245933532715})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.2874854803085327})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8914, 'crossentropy': 0.8770931640625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6802817583084106})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6292370557785034})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5758183002471924})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5469980239868164})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5313433408737183})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5228872299194336})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4958391785621643})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 47635], ['id', 47890], ['id', 46068], ['id', 14878], ['id', 13137]], 'labels': [8, 2, 3, 3, 1], 'scores': [0.9337483233168757, 1.7466709147742385, 2.3409493775060533, 2.701447428403707, 2.9010137178659976]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9312191009521484})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7980504035949707})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7460709810256958})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8301869034767151})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9086619019508362})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0002589225769043})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.7446205078125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7407827377319336})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5808781385421753})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5140005350112915})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5483767986297607})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.4770514667034149})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 46447], ['id', 43176], ['id', 10308], ['id', 16526], ['id', 31310]], 'labels': [2, 2, 2, 4, 0], 'scores': [0.744885647242387, 1.3985148586125757, 1.9496708639337568, 2.3518980204083784, 2.5899193752707674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8395065665245056})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7483034133911133})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.85222327709198})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8221687078475952})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9144647121429443})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.770566463470459})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8930763006210327})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9152442812919617})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9199656248092651})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9085, 'crossentropy': 0.694070849609375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6939265131950378})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5278923511505127})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5330736637115479})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4685969352722168})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5043109655380249})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4744662046432495})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.44735273718833923})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 2231], ['id', 32572], ['id', 27649], ['id', 15699], ['ood', 52044]], 'labels': [8, 6, 3, 2, -1], 'scores': [0.8404078145140801, 1.5396460532511527, 2.0758909649347546, 2.4282240919186027, 2.622093109689402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8789921998977661})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7989281415939331})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7428057789802551})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8489346504211426})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8257670998573303})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.859687328338623})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 1.0235098600387573})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9039, 'crossentropy': 0.714750927734375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7191844582557678})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5950188040733337})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5231984853744507})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5442578792572021})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.4923253059387207})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5175815224647522})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 36810], ['id', 12493], ['id', 47548], ['id', 19294], ['id', 32509]], 'labels': [6, 8, 8, 4, 8], 'scores': [0.7851458277718337, 1.44423745584028, 1.9734487586524434, 2.3319747787824285, 2.542058738496813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8306666612625122})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7828278541564941})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7180885076522827})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7923865914344788})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8372107744216919})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.749456524848938})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8074741363525391})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.626612939453125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6437137126922607})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.539574921131134})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.47943902015686035})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4417864680290222})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43285685777664185})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.44781801104545593})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 8366], ['id', 57972], ['id', 59314], ['id', 27317], ['id', 40944]], 'labels': [8, 4, 9, 5, 1], 'scores': [0.8376319906473657, 1.5411135932157358, 2.0723190430600953, 2.4106506610392513, 2.600157848228055]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8685510158538818})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6797382831573486})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7875175476074219})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7572017908096313})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7656250596046448})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7562178373336792})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8149675726890564})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.892105221748352})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.6974072265625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6687266826629639})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4973076283931732})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4769746661186218})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4436793923377991})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.42215922474861145})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4740820527076721})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.44996893405914307})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 9555], ['id', 52959], ['id', 24851], ['id', 18302], ['id', 52224]], 'labels': [9, 2, 6, 6, 2], 'scores': [0.8524129546317714, 1.5615625563963587, 2.1152243850268038, 2.4805015930607057, 2.6982775135767794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9305468201637268})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6743279695510864})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7066445350646973})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7033677101135254})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7932069301605225})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7297016382217407})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.624461829662323})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7055875062942505})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7300041317939758})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.720119833946228})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.922, 'crossentropy': 0.59073173828125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6984373331069946})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5049277544021606})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.47603780031204224})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4161689877510071})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4122459292411804})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4206288456916809})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.40916937589645386})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.40051764249801636})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 35246], ['id', 28471], ['id', 9046], ['id', 45776], ['id', 150]], 'labels': [8, 2, 4, 7, 4], 'scores': [0.8565598609513003, 1.604559682775836, 2.1849553851424863, 2.547980386446709, 2.7540516941870328]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8930320739746094})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6180135607719421})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6245246529579163})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6392393112182617})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6659075021743774})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7360701560974121})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7646539211273193})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.518400390625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6829211115837097})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4731895327568054})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4781568646430969})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.449552059173584})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.441184937953949})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 30159], ['id', 670], ['id', 36884], ['id', 28657], ['ood', 33397]], 'labels': [3, 3, 2, 5, -1], 'scores': [0.6973197485514655, 1.3178164086705184, 1.8276945005993044, 2.2079469045462528, 2.4310989409749606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8647596836090088})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6459652185440063})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6818846464157104})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6652808785438538})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6976927518844604})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6719563007354736})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8380378484725952})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6844629049301147})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7252028584480286})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.8288934230804443})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.8161734342575073})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9277, 'crossentropy': 0.582113818359375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.652195155620575})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4860858917236328})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.40487200021743774})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37731343507766724})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42327308654785156})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.36761701107025146})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.355586975812912})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 17549], ['id', 1806], ['id', 11489], ['id', 34765], ['id', 36792]], 'labels': [0, 5, 3, 6, 6], 'scores': [0.7947535368027707, 1.523034337356537, 2.0939633319576014, 2.514080678093954, 2.7300430883538116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8636364936828613})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6540019512176514})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.615919828414917})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5992605686187744})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6229859590530396})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6312075853347778})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6991491317749023})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7348419427871704})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.546452734375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6667966842651367})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4808604121208191})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.44916558265686035})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4337981045246124})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39069777727127075})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.37998276948928833})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.38036754727363586})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 41196], ['id', 20476], ['id', 21896], ['id', 37986], ['id', 37686]], 'labels': [9, 5, 8, 4, 0], 'scores': [0.7615644193250168, 1.4612792868604023, 1.986268120399794, 2.341532734193825, 2.562684265917106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7594413757324219})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5449613332748413})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5791628360748291})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5293710231781006})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.651965856552124})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6934754848480225})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6147937774658203})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6381096839904785})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6603700518608093})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7345348000526428})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7476046085357666})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.543613720703125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6124077439308167})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47652414441108704})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4146384596824646})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.37878334522247314})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3844414949417114})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3740016222000122})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36680102348327637})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3507285416126251})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 40976], ['id', 18029], ['id', 583], ['id', 4111], ['ood', 30348]], 'labels': [1, 0, 9, 2, -1], 'scores': [0.8610748241754231, 1.5853783287429155, 2.1913398347850177, 2.540199267001375, 2.7320681024276885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9379017353057861})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5881097316741943})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6239070892333984})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6113815903663635})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5990334749221802})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.608221709728241})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6282024383544922})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6901054382324219})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6804892420768738})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7072959542274475})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9325, 'crossentropy': 0.520418896484375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.663941502571106})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5131362676620483})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4487990736961365})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.41878271102905273})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.39332473278045654})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.41023319959640503})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38405439257621765})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3563263416290283})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36542749404907227})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 52978], ['id', 26162], ['ood', 36107], ['id', 14697], ['ood', 58641]], 'labels': [0, 7, -1, 8, -1], 'scores': [0.7823430205432864, 1.4242599422512856, 1.946709837977922, 2.294939396784117, 2.4899229613526614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9852019548416138})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6762351989746094})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6276617050170898})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6993928551673889})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6888372898101807})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7607966065406799})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6427092552185059})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7489924430847168})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7748911380767822})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.8975877165794373})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7982791662216187})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8079524040222168})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.712406689453125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6511133909225464})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.520519495010376})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.47037798166275024})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4240812659263611})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.42769724130630493})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.43776947259902954})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4014049768447876})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 38760], ['id', 5630], ['id', 22674], ['ood', 49593], ['id', 43592]], 'labels': [9, 1, 3, -1, 6], 'scores': [0.8678798826833254, 1.601222995743854, 2.173879263880809, 2.5614878841444897, 2.7833946112025947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8664019107818604})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6185261011123657})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6554498672485352})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6128032803535461})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6259667277336121})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6428794860839844})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6917027235031128})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6528913378715515})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6726489067077637})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7595951557159424})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.610099609375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6683237552642822})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48302921652793884})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.44524866342544556})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4463793635368347})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.36524277925491333})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38665154576301575})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.41100573539733887})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3583875298500061})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.383899450302124})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 46163], ['id', 31456], ['id', 20072], ['id', 11196], ['id', 12600]], 'labels': [2, 9, 3, 9, 9], 'scores': [0.8427268878952701, 1.5897729586055194, 2.175521441788227, 2.5328764927925125, 2.704355429869481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9422532320022583})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6302902698516846})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.519075870513916})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6425431966781616})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5890312790870667})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7026380300521851})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9293, 'crossentropy': 0.495439208984375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.659346342086792})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4709407687187195})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4522436261177063})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4138421416282654})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44513434171676636})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 28465], ['id', 47513], ['id', 16692], ['id', 2706], ['ood', 50945]], 'labels': [5, 0, 5, 7, -1], 'scores': [0.7365431658921979, 1.3963959365100305, 1.9428859611962537, 2.315221740750186, 2.5321535535335125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8508396148681641})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5683508515357971})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5388966202735901})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6308534741401672})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5785036087036133})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6351420879364014})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.653329074382782})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6042581796646118})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7562028169631958})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.8347697854042053})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6600651741027832})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.48805966796875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6895202398300171})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5038800239562988})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4732512831687927})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4273391664028168})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.42054563760757446})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.390186071395874})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.36355650424957275})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.373414009809494})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.3575776517391205})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.357391357421875})
store['active_learning_steps'][27]['eval_training']['best_epoch']=10
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59927], ['id', 4880], ['id', 8680], ['id', 45806], ['id', 30446]], 'labels': [9, 2, 8, 7, 9], 'scores': [0.7655312592441854, 1.4761734458760891, 2.0365540849395503, 2.4557766004921566, 2.721565961703023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8520809412002563})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5752218961715698})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5451376438140869})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5854178667068481})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5622143149375916})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6886934041976929})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6170446872711182})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6885070204734802})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.455566552734375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6729764938354492})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.502750039100647})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3894215226173401})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3648901581764221})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.37133553624153137})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35383495688438416})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.37255042791366577})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 14649], ['id', 46832], ['id', 7264], ['id', 1380], ['id', 59433]], 'labels': [0, 7, 9, 4, 0], 'scores': [0.9268613721158907, 1.6240926530884794, 2.159158371817779, 2.4963527239423415, 2.6806441548945674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9534636735916138})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5335475206375122})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5643091201782227})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6080774068832397})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5449562668800354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6211340427398682})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5690809488296509})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5903301239013672})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6321951746940613})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7131363153457642})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.50318681640625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.6949740052223206})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.48819243907928467})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.436357319355011})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.3935813307762146})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38566210865974426})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3814753293991089})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3570979833602905})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3710184395313263})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 21601], ['id', 23112], ['id', 56735], ['id', 17621], ['id', 42136]], 'labels': [1, 8, 0, 3, 0], 'scores': [0.7501636444987447, 1.4350461842887343, 1.9274686387573787, 2.267817556069601, 2.4681522000603344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8660271763801575})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4923015832901001})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4639175534248352})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4876178503036499})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4751583933830261})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5219302773475647})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5053993463516235})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5421806573867798})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9487, 'crossentropy': 0.3963489990234375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6850508451461792})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42092660069465637})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40820109844207764})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3868767023086548})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3374059200286865})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.32976800203323364})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3271443843841553})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 27151], ['ood', 32240], ['id', 3118], ['id', 3580], ['id', 12786]], 'labels': [7, -1, 5, 5, 4], 'scores': [0.7230294381320859, 1.3838649120795745, 1.9527412863220128, 2.3515683691693976, 2.5725402487106717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7882422208786011})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5169268846511841})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5406880378723145})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5471183061599731})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6079860925674438})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5856099724769592})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5913193821907043})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9363, 'crossentropy': 0.442040478515625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7388648986816406})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5190032720565796})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45365047454833984})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4143982529640198})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.40414106845855713})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.38830602169036865})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 31738], ['id', 8719], ['id', 8552], ['id', 2831], ['ood', 58209]], 'labels': [8, 8, 2, 1, -1], 'scores': [0.6921730078097597, 1.3229185914516814, 1.8011427370396218, 2.150600511472601, 2.3544036947496894]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8501049280166626})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5000133514404297})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5262610912322998})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5922994613647461})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5331001281738281})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5422563552856445})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5703962445259094})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6145247220993042})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6549890041351318})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.43993984375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.683235764503479})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4641769826412201})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4249448776245117})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38404184579849243})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37527114152908325})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.36302974820137024})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3513268232345581})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33287695050239563})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 3798], ['ood', 25624], ['id', 16882], ['id', 56001], ['ood', 38890]], 'labels': [7, -1, 7, 8, -1], 'scores': [0.747490262536701, 1.3815155467775582, 1.9076257209163936, 2.27065008683363, 2.474654004790515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9608587026596069})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5579760074615479})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5860469341278076})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6213469505310059})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5810075998306274})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5714315176010132})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6004875302314758})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6442086696624756})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.609149694442749})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.7522526979446411})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6466001272201538})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.7322276830673218})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.517382177734375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6488908529281616})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4426153302192688})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3992658257484436})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.35183537006378174})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.36129283905029297})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3465502858161926})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35063010454177856})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3367099463939667})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3295805752277374})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3439435362815857})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 2406], ['id', 33685], ['id', 14635], ['id', 57665], ['ood', 36967]], 'labels': [4, 2, 3, 8, -1], 'scores': [0.8266439652190718, 1.5402484617974612, 2.0923940435302413, 2.4271338001535723, 2.595167745560274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8722679615020752})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5288480520248413})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5183938145637512})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5397717952728271})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5953898429870605})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.47562666015625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6872400045394897})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5430982112884521})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5186010003089905})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49341878294944763})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 59294], ['ood', 50403], ['id', 10028], ['ood', 27863], ['id', 424]], 'labels': [8, -1, 9, -1, 9], 'scores': [0.5374942021757454, 1.0262176854389122, 1.444325203487951, 1.7997639646616852, 2.074952694555318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9432235956192017})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5886411666870117})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5319238305091858})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5820976495742798})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5512570738792419})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6935492753982544})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5364367365837097})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6416566371917725})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6032874584197998})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6254798173904419})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.44432373046875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6852954626083374})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5105794668197632})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4391025900840759})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4070684313774109})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3929749131202698})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3716588616371155})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3683956265449524})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.37109965085983276})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.38043302297592163})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 7793], ['ood', 11446], ['id', 38280], ['id', 57053], ['id', 24290]], 'labels': [8, -1, 5, 0, 2], 'scores': [0.74424847658264, 1.3945308181151757, 1.935564764089671, 2.33064307124629, 2.5733951980864678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.874959409236908})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5299121141433716})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43604326248168945})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5148544907569885})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5446661114692688})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5412610769271851})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.38071083984375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7083984613418579})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5276901721954346})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46579456329345703})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4299222230911255})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.41993460059165955})
store['active_learning_steps'][36]['eval_training']['best_epoch']=4
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 31650], ['id', 57507], ['id', 26733], ['id', 29335], ['id', 56190]], 'labels': [5, 0, 2, 8, 4], 'scores': [0.636134816446938, 1.1379156726746191, 1.571722037642651, 1.9014208991737025, 2.142281809664934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9153016805648804})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5078251361846924})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5017907023429871})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5401324033737183})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.511871874332428})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.472209619140625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7302729487419128})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5594702959060669})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5408132076263428})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4890986680984497})
store['active_learning_steps'][37]['eval_training']['best_epoch']=4
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 15988], ['ood', 29501], ['id', 7851], ['id', 1674], ['id', 15402]], 'labels': [8, -1, 8, 9, 5], 'scores': [0.5674381256947665, 1.0818304065688, 1.5155939085409793, 1.8516544174246032, 2.0845139166711864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.004502296447754})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5636410713195801})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.43703365325927734})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4709544777870178})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5182056427001953})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5246915817260742})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.4017340576171875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7061004638671875})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5438876152038574})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5012319684028625})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.42687565088272095})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4164617359638214})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 7768], ['ood', 50403], ['id', 45801], ['ood', 19837], ['ood', 55181]], 'labels': [8, -1, 3, -1, -1], 'scores': [0.6146169063188986, 1.143110233368358, 1.6037578663180208, 1.966417473104336, 2.2339316132425697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.049991488456726})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5789233446121216})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5112228393554688})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45395416021347046})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5334606170654297})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5021038055419922})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5121601223945618})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9468, 'crossentropy': 0.3800649169921875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7092502117156982})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4783463776111603})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4398212134838104})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.39003151655197144})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3730810880661011})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3578298091888428})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 54880], ['id', 12558], ['id', 44172], ['id', 37315], ['id', 16190]], 'labels': [5, 7, 8, 6, 3], 'scores': [0.6732395239592068, 1.2467971458275748, 1.7189232053987697, 2.07432870092509, 2.3221581063885646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9804198741912842})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5992471575737})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5257009267807007})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5165653228759766})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5024968981742859})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.523496150970459})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5280598402023315})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5395586490631104})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5301800966262817})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5640714764595032})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5404706001281738})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6125127077102661})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.406849853515625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6995203495025635})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4840694069862366})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.41163915395736694})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3685396909713745})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3523206114768982})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.34342145919799805})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.32389146089553833})
store['active_learning_steps'][40]['eval_training']['best_epoch']=4
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 50714], ['ood', 7949], ['id', 32417], ['ood', 13195], ['ood', 11690]], 'labels': [8, -1, 9, -1, -1], 'scores': [0.7306582756750117, 1.3964293256378948, 1.9577468986573017, 2.336334231043236, 2.556428593916742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.065709114074707})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6015156507492065})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4683706760406494})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45303183794021606})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5356095433235168})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5354830026626587})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4739936590194702})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.4236380859375}
